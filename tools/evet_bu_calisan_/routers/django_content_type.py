from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.django_content_type import DjangoContentType, DjangoContentTypeCreate
from models.django_content_type import DjangoContentType as DBDjangoContentType
from crud.django_content_type import get_all_django_content_type, get_django_content_type_by_id, create_django_content_type

router = APIRouter(prefix='/django_content_type', tags=['DjangoContentType'])

@router.get('/', response_model=list[DjangoContentType])
async def list_django_content_type(db: AsyncSession = Depends()):
    return await get_all_django_content_type(db)

@router.get('/{id}', response_model=DjangoContentType)
async def get_django_content_type_item(id: int, db: AsyncSession = Depends()):
    result = await get_django_content_type_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DjangoContentType)
async def create_django_content_type_item(data: DjangoContentTypeCreate, db: AsyncSession = Depends()):
    db_item = DBDjangoContentType(**data.dict())
    return await create_django_content_type(db, db_item)