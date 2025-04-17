from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.alinan_siparis import AlinanSiparis, AlinanSiparisCreate
from models.alinan_siparis import AlinanSiparis as DBAlinanSiparis
from crud.alinan_siparis import get_all_alinan_siparis, get_alinan_siparis_by_id, create_alinan_siparis

router = APIRouter(prefix='/alinan_siparis', tags=['AlinanSiparis'])

@router.get('/', response_model=list[AlinanSiparis])
async def list_alinan_siparis(db: AsyncSession = Depends()):
    return await get_all_alinan_siparis(db)

@router.get('/{id}', response_model=AlinanSiparis)
async def get_alinan_siparis_item(id: int, db: AsyncSession = Depends()):
    result = await get_alinan_siparis_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AlinanSiparis)
async def create_alinan_siparis_item(data: AlinanSiparisCreate, db: AsyncSession = Depends()):
    db_item = DBAlinanSiparis(**data.dict())
    return await create_alinan_siparis(db, db_item)