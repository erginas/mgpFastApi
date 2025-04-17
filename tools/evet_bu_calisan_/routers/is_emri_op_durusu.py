from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.is_emri_op_durusu import IsEmriOpDurusu, IsEmriOpDurusuCreate
from models.is_emri_op_durusu import IsEmriOpDurusu as DBIsEmriOpDurusu
from crud.is_emri_op_durusu import get_all_is_emri_op_durusu, get_is_emri_op_durusu_by_id, create_is_emri_op_durusu

router = APIRouter(prefix='/is_emri_op_durusu', tags=['IsEmriOpDurusu'])

@router.get('/', response_model=list[IsEmriOpDurusu])
async def list_is_emri_op_durusu(db: AsyncSession = Depends()):
    return await get_all_is_emri_op_durusu(db)

@router.get('/{id}', response_model=IsEmriOpDurusu)
async def get_is_emri_op_durusu_item(id: int, db: AsyncSession = Depends()):
    result = await get_is_emri_op_durusu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=IsEmriOpDurusu)
async def create_is_emri_op_durusu_item(data: IsEmriOpDurusuCreate, db: AsyncSession = Depends()):
    db_item = DBIsEmriOpDurusu(**data.dict())
    return await create_is_emri_op_durusu(db, db_item)