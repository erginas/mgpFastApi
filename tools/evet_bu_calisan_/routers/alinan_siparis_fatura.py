from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.alinan_siparis_fatura import AlinanSiparisFatura, AlinanSiparisFaturaCreate
from models.alinan_siparis_fatura import AlinanSiparisFatura as DBAlinanSiparisFatura
from crud.alinan_siparis_fatura import get_all_alinan_siparis_fatura, get_alinan_siparis_fatura_by_id, create_alinan_siparis_fatura

router = APIRouter(prefix='/alinan_siparis_fatura', tags=['AlinanSiparisFatura'])

@router.get('/', response_model=list[AlinanSiparisFatura])
async def list_alinan_siparis_fatura(db: AsyncSession = Depends()):
    return await get_all_alinan_siparis_fatura(db)

@router.get('/{id}', response_model=AlinanSiparisFatura)
async def get_alinan_siparis_fatura_item(id: int, db: AsyncSession = Depends()):
    result = await get_alinan_siparis_fatura_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AlinanSiparisFatura)
async def create_alinan_siparis_fatura_item(data: AlinanSiparisFaturaCreate, db: AsyncSession = Depends()):
    db_item = DBAlinanSiparisFatura(**data.dict())
    return await create_alinan_siparis_fatura(db, db_item)