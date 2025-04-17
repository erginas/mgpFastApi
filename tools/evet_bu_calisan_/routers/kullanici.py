from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kullanici import Kullanici, KullaniciCreate
from models.kullanici import Kullanici as DBKullanici
from crud.kullanici import get_all_kullanici, get_kullanici_by_id, create_kullanici

router = APIRouter(prefix='/kullanici', tags=['Kullanici'])

@router.get('/', response_model=list[Kullanici])
async def list_kullanici(db: AsyncSession = Depends()):
    return await get_all_kullanici(db)

@router.get('/{id}', response_model=Kullanici)
async def get_kullanici_item(id: int, db: AsyncSession = Depends()):
    result = await get_kullanici_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Kullanici)
async def create_kullanici_item(data: KullaniciCreate, db: AsyncSession = Depends()):
    db_item = DBKullanici(**data.dict())
    return await create_kullanici(db, db_item)