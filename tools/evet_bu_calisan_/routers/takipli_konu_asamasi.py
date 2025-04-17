from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.takipli_konu_asamasi import TakipliKonuAsamasi, TakipliKonuAsamasiCreate
from models.takipli_konu_asamasi import TakipliKonuAsamasi as DBTakipliKonuAsamasi
from crud.takipli_konu_asamasi import get_all_takipli_konu_asamasi, get_takipli_konu_asamasi_by_id, create_takipli_konu_asamasi

router = APIRouter(prefix='/takipli_konu_asamasi', tags=['TakipliKonuAsamasi'])

@router.get('/', response_model=list[TakipliKonuAsamasi])
async def list_takipli_konu_asamasi(db: AsyncSession = Depends()):
    return await get_all_takipli_konu_asamasi(db)

@router.get('/{id}', response_model=TakipliKonuAsamasi)
async def get_takipli_konu_asamasi_item(id: int, db: AsyncSession = Depends()):
    result = await get_takipli_konu_asamasi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TakipliKonuAsamasi)
async def create_takipli_konu_asamasi_item(data: TakipliKonuAsamasiCreate, db: AsyncSession = Depends()):
    db_item = DBTakipliKonuAsamasi(**data.dict())
    return await create_takipli_konu_asamasi(db, db_item)