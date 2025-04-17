from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kisi_yetkinligi import KisiYetkinligi, KisiYetkinligiCreate
from models.kisi_yetkinligi import KisiYetkinligi as DBKisiYetkinligi
from crud.kisi_yetkinligi import get_all_kisi_yetkinligi, get_kisi_yetkinligi_by_id, create_kisi_yetkinligi

router = APIRouter(prefix='/kisi_yetkinligi', tags=['KisiYetkinligi'])

@router.get('/', response_model=list[KisiYetkinligi])
async def list_kisi_yetkinligi(db: AsyncSession = Depends()):
    return await get_all_kisi_yetkinligi(db)

@router.get('/{id}', response_model=KisiYetkinligi)
async def get_kisi_yetkinligi_item(id: int, db: AsyncSession = Depends()):
    result = await get_kisi_yetkinligi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=KisiYetkinligi)
async def create_kisi_yetkinligi_item(data: KisiYetkinligiCreate, db: AsyncSession = Depends()):
    db_item = DBKisiYetkinligi(**data.dict())
    return await create_kisi_yetkinligi(db, db_item)