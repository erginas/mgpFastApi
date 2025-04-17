from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.alinan_siparis_detay import AlinanSiparisDetay, AlinanSiparisDetayCreate
from models.alinan_siparis_detay import AlinanSiparisDetay as DBAlinanSiparisDetay
from crud.alinan_siparis_detay import get_all_alinan_siparis_detay, get_alinan_siparis_detay_by_id, create_alinan_siparis_detay

router = APIRouter(prefix='/alinan_siparis_detay', tags=['AlinanSiparisDetay'])

@router.get('/', response_model=list[AlinanSiparisDetay])
async def list_alinan_siparis_detay(db: AsyncSession = Depends()):
    return await get_all_alinan_siparis_detay(db)

@router.get('/{id}', response_model=AlinanSiparisDetay)
async def get_alinan_siparis_detay_item(id: int, db: AsyncSession = Depends()):
    result = await get_alinan_siparis_detay_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AlinanSiparisDetay)
async def create_alinan_siparis_detay_item(data: AlinanSiparisDetayCreate, db: AsyncSession = Depends()):
    db_item = DBAlinanSiparisDetay(**data.dict())
    return await create_alinan_siparis_detay(db, db_item)