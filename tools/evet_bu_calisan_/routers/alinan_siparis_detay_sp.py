from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.alinan_siparis_detay_sp import AlinanSiparisDetaySp, AlinanSiparisDetaySpCreate
from models.alinan_siparis_detay_sp import AlinanSiparisDetaySp as DBAlinanSiparisDetaySp
from crud.alinan_siparis_detay_sp import get_all_alinan_siparis_detay_sp, get_alinan_siparis_detay_sp_by_id, create_alinan_siparis_detay_sp

router = APIRouter(prefix='/alinan_siparis_detay_sp', tags=['AlinanSiparisDetaySp'])

@router.get('/', response_model=list[AlinanSiparisDetaySp])
async def list_alinan_siparis_detay_sp(db: AsyncSession = Depends()):
    return await get_all_alinan_siparis_detay_sp(db)

@router.get('/{id}', response_model=AlinanSiparisDetaySp)
async def get_alinan_siparis_detay_sp_item(id: int, db: AsyncSession = Depends()):
    result = await get_alinan_siparis_detay_sp_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AlinanSiparisDetaySp)
async def create_alinan_siparis_detay_sp_item(data: AlinanSiparisDetaySpCreate, db: AsyncSession = Depends()):
    db_item = DBAlinanSiparisDetaySp(**data.dict())
    return await create_alinan_siparis_detay_sp(db, db_item)