from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.alinan_siparis_fatura_detay import AlinanSiparisFaturaDetay, AlinanSiparisFaturaDetayCreate
from models.alinan_siparis_fatura_detay import AlinanSiparisFaturaDetay as DBAlinanSiparisFaturaDetay
from crud.alinan_siparis_fatura_detay import get_all_alinan_siparis_fatura_detay, get_alinan_siparis_fatura_detay_by_id, create_alinan_siparis_fatura_detay

router = APIRouter(prefix='/alinan_siparis_fatura_detay', tags=['AlinanSiparisFaturaDetay'])

@router.get('/', response_model=list[AlinanSiparisFaturaDetay])
async def list_alinan_siparis_fatura_detay(db: AsyncSession = Depends()):
    return await get_all_alinan_siparis_fatura_detay(db)

@router.get('/{id}', response_model=AlinanSiparisFaturaDetay)
async def get_alinan_siparis_fatura_detay_item(id: int, db: AsyncSession = Depends()):
    result = await get_alinan_siparis_fatura_detay_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AlinanSiparisFaturaDetay)
async def create_alinan_siparis_fatura_detay_item(data: AlinanSiparisFaturaDetayCreate, db: AsyncSession = Depends()):
    db_item = DBAlinanSiparisFaturaDetay(**data.dict())
    return await create_alinan_siparis_fatura_detay(db, db_item)