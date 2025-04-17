from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.takipli_konu_birimi import TakipliKonuBirimi, TakipliKonuBirimiCreate
from models.takipli_konu_birimi import TakipliKonuBirimi as DBTakipliKonuBirimi
from crud.takipli_konu_birimi import get_all_takipli_konu_birimi, get_takipli_konu_birimi_by_id, create_takipli_konu_birimi

router = APIRouter(prefix='/takipli_konu_birimi', tags=['TakipliKonuBirimi'])

@router.get('/', response_model=list[TakipliKonuBirimi])
async def list_takipli_konu_birimi(db: AsyncSession = Depends()):
    return await get_all_takipli_konu_birimi(db)

@router.get('/{id}', response_model=TakipliKonuBirimi)
async def get_takipli_konu_birimi_item(id: int, db: AsyncSession = Depends()):
    result = await get_takipli_konu_birimi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TakipliKonuBirimi)
async def create_takipli_konu_birimi_item(data: TakipliKonuBirimiCreate, db: AsyncSession = Depends()):
    db_item = DBTakipliKonuBirimi(**data.dict())
    return await create_takipli_konu_birimi(db, db_item)