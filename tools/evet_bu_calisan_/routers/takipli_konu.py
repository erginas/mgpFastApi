from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.takipli_konu import TakipliKonu, TakipliKonuCreate
from models.takipli_konu import TakipliKonu as DBTakipliKonu
from crud.takipli_konu import get_all_takipli_konu, get_takipli_konu_by_id, create_takipli_konu

router = APIRouter(prefix='/takipli_konu', tags=['TakipliKonu'])

@router.get('/', response_model=list[TakipliKonu])
async def list_takipli_konu(db: AsyncSession = Depends()):
    return await get_all_takipli_konu(db)

@router.get('/{id}', response_model=TakipliKonu)
async def get_takipli_konu_item(id: int, db: AsyncSession = Depends()):
    result = await get_takipli_konu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TakipliKonu)
async def create_takipli_konu_item(data: TakipliKonuCreate, db: AsyncSession = Depends()):
    db_item = DBTakipliKonu(**data.dict())
    return await create_takipli_konu(db, db_item)