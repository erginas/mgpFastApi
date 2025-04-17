from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.is_emri_reservesi import IsEmriReservesi, IsEmriReservesiCreate
from models.is_emri_reservesi import IsEmriReservesi as DBIsEmriReservesi
from crud.is_emri_reservesi import get_all_is_emri_reservesi, get_is_emri_reservesi_by_id, create_is_emri_reservesi

router = APIRouter(prefix='/is_emri_reservesi', tags=['IsEmriReservesi'])

@router.get('/', response_model=list[IsEmriReservesi])
async def list_is_emri_reservesi(db: AsyncSession = Depends()):
    return await get_all_is_emri_reservesi(db)

@router.get('/{id}', response_model=IsEmriReservesi)
async def get_is_emri_reservesi_item(id: int, db: AsyncSession = Depends()):
    result = await get_is_emri_reservesi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=IsEmriReservesi)
async def create_is_emri_reservesi_item(data: IsEmriReservesiCreate, db: AsyncSession = Depends()):
    db_item = DBIsEmriReservesi(**data.dict())
    return await create_is_emri_reservesi(db, db_item)