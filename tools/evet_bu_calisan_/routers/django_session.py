from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.django_session import DjangoSession, DjangoSessionCreate
from models.django_session import DjangoSession as DBDjangoSession
from crud.django_session import get_all_django_session, get_django_session_by_id, create_django_session

router = APIRouter(prefix='/django_session', tags=['DjangoSession'])

@router.get('/', response_model=list[DjangoSession])
async def list_django_session(db: AsyncSession = Depends()):
    return await get_all_django_session(db)

@router.get('/{id}', response_model=DjangoSession)
async def get_django_session_item(id: int, db: AsyncSession = Depends()):
    result = await get_django_session_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DjangoSession)
async def create_django_session_item(data: DjangoSessionCreate, db: AsyncSession = Depends()):
    db_item = DBDjangoSession(**data.dict())
    return await create_django_session(db, db_item)