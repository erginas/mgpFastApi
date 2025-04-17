from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.is_emri_operasyon_durusu import IsEmriOperasyonDurusu, IsEmriOperasyonDurusuCreate
from models.is_emri_operasyon_durusu import IsEmriOperasyonDurusu as DBIsEmriOperasyonDurusu
from crud.is_emri_operasyon_durusu import get_all_is_emri_operasyon_durusu, get_is_emri_operasyon_durusu_by_id, create_is_emri_operasyon_durusu

router = APIRouter(prefix='/is_emri_operasyon_durusu', tags=['IsEmriOperasyonDurusu'])

@router.get('/', response_model=list[IsEmriOperasyonDurusu])
async def list_is_emri_operasyon_durusu(db: AsyncSession = Depends()):
    return await get_all_is_emri_operasyon_durusu(db)

@router.get('/{id}', response_model=IsEmriOperasyonDurusu)
async def get_is_emri_operasyon_durusu_item(id: int, db: AsyncSession = Depends()):
    result = await get_is_emri_operasyon_durusu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=IsEmriOperasyonDurusu)
async def create_is_emri_operasyon_durusu_item(data: IsEmriOperasyonDurusuCreate, db: AsyncSession = Depends()):
    db_item = DBIsEmriOperasyonDurusu(**data.dict())
    return await create_is_emri_operasyon_durusu(db, db_item)