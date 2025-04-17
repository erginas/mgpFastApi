from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.is_emri_aktarma_islemi import IsEmriAktarmaIslemi, IsEmriAktarmaIslemiCreate
from models.is_emri_aktarma_islemi import IsEmriAktarmaIslemi as DBIsEmriAktarmaIslemi
from crud.is_emri_aktarma_islemi import get_all_is_emri_aktarma_islemi, get_is_emri_aktarma_islemi_by_id, create_is_emri_aktarma_islemi

router = APIRouter(prefix='/is_emri_aktarma_islemi', tags=['IsEmriAktarmaIslemi'])

@router.get('/', response_model=list[IsEmriAktarmaIslemi])
async def list_is_emri_aktarma_islemi(db: AsyncSession = Depends()):
    return await get_all_is_emri_aktarma_islemi(db)

@router.get('/{id}', response_model=IsEmriAktarmaIslemi)
async def get_is_emri_aktarma_islemi_item(id: int, db: AsyncSession = Depends()):
    result = await get_is_emri_aktarma_islemi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=IsEmriAktarmaIslemi)
async def create_is_emri_aktarma_islemi_item(data: IsEmriAktarmaIslemiCreate, db: AsyncSession = Depends()):
    db_item = DBIsEmriAktarmaIslemi(**data.dict())
    return await create_is_emri_aktarma_islemi(db, db_item)