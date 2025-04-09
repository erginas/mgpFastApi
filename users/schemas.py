from datetime import datetime
from pydantic import BaseModel, UUID4,  EmailStr, field_validator
from pydantic import FieldValidationInfo
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr
    full_name: str

    class Config:
        from_attributes = True


    # def __init__(self, **kwargs):
    #     print("Veri:", kwargs)  # Debug için
    #     super().__init__(**kwargs)

class UserCreate(UserBase):
    password: str
    class Config:
        from_attributes = True


class User(UserBase):
    id: UUID4

    class Config:
        from_attributes = True

    @field_validator("id")
    def convert_to_str(cls, v, values, **kwargs):
        # Eğer UUID geçerli bir string formatında ise, onu UUID4'e dönüştür
        try:
            if isinstance(v, str):
                return UUID(v)  # String'i UUID'ye dönüştür
            return v  # Eğer zaten UUID ise, olduğu gibi döndür
        except ValueError:
            raise ValueError(f"Invalid UUID string: {v}")


class UserRegister(UserBase):
    password: str
    confirm_password: str

    @field_validator("confirm_password")
    def verify_password_match(cls, v, info: FieldValidationInfo):
        password = info.data["password"]
        if v != password:
            raise ValueError("The two passwords did not match.")
        return v


class UserLogin(BaseModel):
    email: EmailStr
    password: str
    class Config:
        from_attributes = True

class JwtTokenSchema(BaseModel):
    token: str
    payload: dict
    expire: datetime
    class Config:
        from_attributes = True

class TokenPair(BaseModel):
    access: JwtTokenSchema
    refresh: JwtTokenSchema
    class Config:
        from_attributes = True

class RefreshToken(BaseModel):
    refresh: str

    class Config:
        from_attributes = True
class SuccessResponseScheme(BaseModel):
    msg: str
    class Config:
        from_attributes = True

class BlackListToken(BaseModel):
    id: UUID4
    expire: datetime

    class Config:
        from_attributes = True


class MailBodySchema(BaseModel):
    token: str
    type: str
    class Config:
        from_attributes = True

class EmailSchema(BaseModel):
    recipients: list[EmailStr]
    subject: str
    body: MailBodySchema
    class Config:
        from_attributes = True



class MailTaskSchema(BaseModel):
    user: User
    body: MailBodySchema

    class Config:
        from_attributes = True

class ForgotPasswordSchema(BaseModel):
    email: EmailStr
    class Config:
        from_attributes = True

class PasswordResetSchema(BaseModel):
    password: str
    confirm_password: str
    class Config:
        from_attributes = True
    @field_validator("confirm_password")
    def verify_password_match(cls, v, values, **kwargs):
        password = values.get("password")

        if v != password:
            raise ValueError("The two passwords did not match.")

        return v


class PasswordUpdateSchema(PasswordResetSchema):
    old_password: str
    class Config:
        from_attributes = True

class OldPasswordErrorSchema(BaseModel):
    old_password: bool
    class Config:
        from_attributes = True
    @field_validator("old_password")
    def check_old_password_status(cls, v, values, **kwargs):
        if not v:
            raise ValueError("Old password is not corret")


# class ArticleCreateSchema(BaseModel):
#     title: str
#     content: str
#     class Config:
#         from_attributes = True
#
# class ArticleListScheme(ArticleCreateSchema):
#     id: UUID4
#     author_id: UUID4
#
#     class Config:
#         from_attributes = True
#
# class AkatarmaCreateSchema(BaseModel):
#     stok_kodu: str
#     malzeme_no: str
#     class Config:
#         from_attributes = True
#
# class AkatarmaListScheme(ArticleCreateSchema):
#     stok_kodu: str
#     malzeme_no: str
#
#     class Config:
#         from_attributes = True
