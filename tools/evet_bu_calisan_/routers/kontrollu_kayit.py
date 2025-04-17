from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kontrollu_kayit import KontrolluKayit, KontrolluKayitCreate
from models.kontrollu_kayit import KontrolluKayit as DBKontrolluKayit
from crud.kontrollu_kayit import get_all_kontrollu_kayit, get_kontrollu_kayit_by_id, create_kontrollu_kayit

router = APIRouter(prefix='/kontrollu_kayit', tags=['KontrolluKayit'])

@router.get('/', response_model=list[KontrolluKayit])
async def list_kontrollu_kayit(db: AsyncSession = Depends()):
    return await get_all_kontrollu_kayit(db)

@router.get('/{id}', response_model=KontrolluKayit)
async def get_kontrollu_kayit_item(id: int, db: AsyncSession = Depends()):
    result = await get_kontrollu_kayit_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=KontrolluKayit)
async def create_kontrollu_kayit_item(data: KontrolluKayitCreate, db: AsyncSession = Depends()):
    db_item = DBKontrolluKayit(**data.dict())
    return await create_kontrollu_kayit(db, db_item)