from datetime import datetime
from sqlalchemy.future import select
from typing import List
import uuid

from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks, Response, Cookie
from fastapi.exceptions import RequestValidationError
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from pydantic import ValidationError
from starlette import status

from core.database import SessionFactory as get_db
#from users.dependencies import get_db


from users import schemas, models
from users.core.hash import get_password_hash, verify_password
from users.core.jwt import (
    create_token_pair,
    refresh_token_state,
    decode_access_token,
    mail_token,
    add_refresh_token_cookie,
    SUB,
    JTI,
    EXP, verify_access_token,
)
from users.exceptions import BadRequestException, NotFoundException, ForbiddenException
from users.models import User
from users.schemas import UserProfile
from users.tasks import (
    user_mail_event,
)

from fastapi import APIRouter
user_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@user_router.post("/register", response_model=schemas.User)
async def register(
    data: schemas.UserRegister,
    bg_task: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    user = await models.User.find_by_email(db=db, email=data.email)
    if user:
        raise HTTPException(status_code=400, detail="Email has already registered")

    # Hash password
    user_data = data.dict(exclude={"confirm_password"})
    user_data["password"] = get_password_hash(user_data["password"])

    # Create user instance
    user = models.User(**user_data)
    user.is_active = False

    db.add(user)
    await db.commit()
    await db.refresh(user)

    # Send verification mail
    user_schema = schemas.User.from_orm(user)
    verify_token = mail_token(user_schema)

    mail_task_data = schemas.MailTaskSchema(
        user=user_schema,
        body=schemas.MailBodySchema(type="verify", token=verify_token),
    )
    bg_task.add_task(user_mail_event, mail_task_data)

    return user_schema


@user_router.post("/login")
async def login(
    data: schemas.UserLogin,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    user = await models.User.authenticate(
        db=db, email=data.email, password=data.password
    )

    if not user:
        raise BadRequestException(detail="Incorrect email or password")

    if not user.is_active:
        raise ForbiddenException()

    user = schemas.User.from_orm(user)

    token_pair = create_token_pair(user=user)

    add_refresh_token_cookie(response=response, token=token_pair.refresh.token)

    return {"token": token_pair.access.token}


@user_router.post("/refresh")
async def refresh(refresh: str = Cookie(None)):
    if not refresh:
        raise BadRequestException(detail="Refresh token required")
    return refresh_token_state(token=refresh)


@user_router.get("/verify", response_model=schemas.SuccessResponseScheme)
async def verify(token: str, db: AsyncSession = Depends(get_db)):
    payload = await decode_access_token(token=token, db=db)
    user = await models.User.find_by_id(db=db, id=payload[SUB])
    if not user:
        raise NotFoundException(detail="User not found")

    user.is_active = True
    await user.save(db=db)
    return {"msg": "Successfully activated"}


@user_router.post("/logout", response_model=schemas.SuccessResponseScheme)
async def logout(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
):
    payload = await decode_access_token(token=token, db=db)
    black_listed = models.BlackListToken(
        id=payload["jti"],  # JTI sabitini doğrudan yazdım, istersen constant tanımı da yaparız
        expire=datetime.utcfromtimestamp(payload["exp"])
    )
    await black_listed.save(db=db)
    return {"msg": "Successfully logged out"}

@user_router.get("/me", response_model=schemas.User)
async def get_my_profile(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
):
    payload = await decode_access_token(token=token, db=db)
    user = await models.User.find_by_id(db=db, id=payload["sub"])
    if not user:
        raise NotFoundException(detail="User not found")

    return schemas.User.from_orm(user)


@user_router.get("/profile", response_model=UserProfile)
async def get_user_profile(db: AsyncSession = Depends(get_db)):
    # SQLAlchemy 2.0 select() kullanımı
    stmt = select(User).limit(1)  # Burada sadece User modelini seçiyoruz
    result = await db.execute(stmt)  # Veritabanı üzerinde sorguyu çalıştırıyoruz

    user = result.scalars().first()  # Sonuçtan ilk kullanıcıyı alıyoruz

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user  # FastAPI, orm_mode sayesinde otomatik dönüşüm yapacak


@user_router.put("/profile", response_model=schemas.User)
async def update_my_profile(
        data: schemas.UserUpdate,
        token: str = Depends(oauth2_scheme),
        db: AsyncSession = Depends(get_db),
):
    from uuid import UUID
    payload = await decode_access_token(token=token, db=db)
    user = await models.User.find_by_id(db=db, id=UUID(payload["sub"]))

    if not user:
        raise NotFoundException(detail="User not found")

    # Güncellenebilir tüm alanları tek tek kontrol et
    if data.title is not None:
        user.title = data.title
    if data.profile_path is not None:
        user.profile_path = data.profile_path
    if data.full_name is not None:
        user.full_name = data.full_name
    # if data.email is not None:
    #     user.email = data.email
    # if data.department is not None:
    #     user.department = data.department
    # if data.phone is not None:
    #     user.phone = data.phone

    await user.save(db=db)
    return schemas.User.from_orm(user)

@user_router.post("/forgot-password", response_model=schemas.SuccessResponseScheme)
async def forgot_password(
    data: schemas.ForgotPasswordSchema,
    bg_task: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    user = await models.User.find_by_email(db=db, email=data.email)
    if user:
        user_schema = schemas.User.from_orm(user)
        reset_token = mail_token(user_schema)

        mail_task_data = schemas.MailTaskSchema(
            user=user_schema,
            body=schemas.MailBodySchema(type="password-reset", token=reset_token),
        )
        bg_task.add_task(user_mail_event, mail_task_data)

    return {"msg": "Reset token sended successfully your email check your email"}


@user_router.post("/password-reset", response_model=schemas.SuccessResponseScheme)
async def password_reset_token(
    token: str,
    data: schemas.PasswordResetSchema,
    db: AsyncSession = Depends(get_db),
):
    payload = await decode_access_token(token=token, db=db)
    user = await models.User.find_by_id(db=db, id=payload[SUB])
    if not user:
        raise NotFoundException(detail="User not found")

    user.password = get_password_hash(data.password)
    await user.save(db=db)

    return {"msg": "Password succesfully updated"}


@user_router.post("/password-update", response_model=schemas.SuccessResponseScheme)
async def password_update(
    data: schemas.PasswordUpdateSchema,
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
):
    payload = await decode_access_token(token=token, db=db)
    user = await models.User.find_by_id(db=db, id=payload["sub"])
    if not user:
        raise NotFoundException(detail="User not found")

    if not verify_password(data.old_password, user.password):
        # ValidationException örneği dönmek yerine elle raise edelim:
        raise RequestValidationError([
            {
                "loc": ["body", "old_password"],
                "msg": "Incorrect old password",
                "type": "value_error",
            }
        ])

    user.password = get_password_hash(data.password)
    await user.save(db=db)

    return {"msg": "Successfully updated"}

