from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.alinan_siparis_sevkiyati import AlinanSiparisSevkiyati, AlinanSiparisSevkiyatiCreate
from models.alinan_siparis_sevkiyati import AlinanSiparisSevkiyati as DBAlinanSiparisSevkiyati
from crud.alinan_siparis_sevkiyati import get_all_alinan_siparis_sevkiyati, get_alinan_siparis_sevkiyati_by_id, create_alinan_siparis_sevkiyati

router = APIRouter(prefix='/alinan_siparis_sevkiyati', tags=['AlinanSiparisSevkiyati'])

@router.get('/', response_model=list[AlinanSiparisSevkiyati])
async def list_alinan_siparis_sevkiyati(db: AsyncSession = Depends()):
    return await get_all_alinan_siparis_sevkiyati(db)

@router.get('/{id}', response_model=AlinanSiparisSevkiyati)
async def get_alinan_siparis_sevkiyati_item(id: int, db: AsyncSession = Depends()):
    result = await get_alinan_siparis_sevkiyati_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AlinanSiparisSevkiyati)
async def create_alinan_siparis_sevkiyati_item(data: AlinanSiparisSevkiyatiCreate, db: AsyncSession = Depends()):
    db_item = DBAlinanSiparisSevkiyati(**data.dict())
    return await create_alinan_siparis_sevkiyati(db, db_item)