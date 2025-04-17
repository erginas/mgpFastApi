from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_tedarik_fiyat_detay import MalzemeTedarikFiyatDetay, MalzemeTedarikFiyatDetayCreate
from models.malzeme_tedarik_fiyat_detay import MalzemeTedarikFiyatDetay as DBMalzemeTedarikFiyatDetay
from crud.malzeme_tedarik_fiyat_detay import get_all_malzeme_tedarik_fiyat_detay, get_malzeme_tedarik_fiyat_detay_by_id, create_malzeme_tedarik_fiyat_detay

router = APIRouter(prefix='/malzeme_tedarik_fiyat_detay', tags=['MalzemeTedarikFiyatDetay'])

@router.get('/', response_model=list[MalzemeTedarikFiyatDetay])
async def list_malzeme_tedarik_fiyat_detay(db: AsyncSession = Depends()):
    return await get_all_malzeme_tedarik_fiyat_detay(db)

@router.get('/{id}', response_model=MalzemeTedarikFiyatDetay)
async def get_malzeme_tedarik_fiyat_detay_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_tedarik_fiyat_detay_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeTedarikFiyatDetay)
async def create_malzeme_tedarik_fiyat_detay_item(data: MalzemeTedarikFiyatDetayCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeTedarikFiyatDetay(**data.dict())
    return await create_malzeme_tedarik_fiyat_detay(db, db_item)