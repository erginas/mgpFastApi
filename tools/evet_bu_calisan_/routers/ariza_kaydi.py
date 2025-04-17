from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.ariza_kaydi import ArizaKaydi, ArizaKaydiCreate
from models.ariza_kaydi import ArizaKaydi as DBArizaKaydi
from crud.ariza_kaydi import get_all_ariza_kaydi, get_ariza_kaydi_by_id, create_ariza_kaydi

router = APIRouter(prefix='/ariza_kaydi', tags=['ArizaKaydi'])

@router.get('/', response_model=list[ArizaKaydi])
async def list_ariza_kaydi(db: AsyncSession = Depends()):
    return await get_all_ariza_kaydi(db)

@router.get('/{id}', response_model=ArizaKaydi)
async def get_ariza_kaydi_item(id: int, db: AsyncSession = Depends()):
    result = await get_ariza_kaydi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ArizaKaydi)
async def create_ariza_kaydi_item(data: ArizaKaydiCreate, db: AsyncSession = Depends()):
    db_item = DBArizaKaydi(**data.dict())
    return await create_ariza_kaydi(db, db_item)