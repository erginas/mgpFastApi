from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.is_emri_planlanan_adim import IsEmriPlanlananAdim, IsEmriPlanlananAdimCreate
from models.is_emri_planlanan_adim import IsEmriPlanlananAdim as DBIsEmriPlanlananAdim
from crud.is_emri_planlanan_adim import get_all_is_emri_planlanan_adim, get_is_emri_planlanan_adim_by_id, create_is_emri_planlanan_adim

router = APIRouter(prefix='/is_emri_planlanan_adim', tags=['IsEmriPlanlananAdim'])

@router.get('/', response_model=list[IsEmriPlanlananAdim])
async def list_is_emri_planlanan_adim(db: AsyncSession = Depends()):
    return await get_all_is_emri_planlanan_adim(db)

@router.get('/{id}', response_model=IsEmriPlanlananAdim)
async def get_is_emri_planlanan_adim_item(id: int, db: AsyncSession = Depends()):
    result = await get_is_emri_planlanan_adim_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=IsEmriPlanlananAdim)
async def create_is_emri_planlanan_adim_item(data: IsEmriPlanlananAdimCreate, db: AsyncSession = Depends()):
    db_item = DBIsEmriPlanlananAdim(**data.dict())
    return await create_is_emri_planlanan_adim(db, db_item)