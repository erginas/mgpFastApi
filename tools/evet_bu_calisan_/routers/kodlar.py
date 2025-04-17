from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kodlar import Kodlar, KodlarCreate
from models.kodlar import Kodlar as DBKodlar
from crud.kodlar import get_all_kodlar, get_kodlar_by_id, create_kodlar

router = APIRouter(prefix='/kodlar', tags=['Kodlar'])

@router.get('/', response_model=list[Kodlar])
async def list_kodlar(db: AsyncSession = Depends()):
    return await get_all_kodlar(db)

@router.get('/{id}', response_model=Kodlar)
async def get_kodlar_item(id: int, db: AsyncSession = Depends()):
    result = await get_kodlar_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Kodlar)
async def create_kodlar_item(data: KodlarCreate, db: AsyncSession = Depends()):
    db_item = DBKodlar(**data.dict())
    return await create_kodlar(db, db_item)