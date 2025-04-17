from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.alinan_siparis_termin_takibi import AlinanSiparisTerminTakibi, AlinanSiparisTerminTakibiCreate
from models.alinan_siparis_termin_takibi import AlinanSiparisTerminTakibi as DBAlinanSiparisTerminTakibi
from crud.alinan_siparis_termin_takibi import get_all_alinan_siparis_termin_takibi, get_alinan_siparis_termin_takibi_by_id, create_alinan_siparis_termin_takibi

router = APIRouter(prefix='/alinan_siparis_termin_takibi', tags=['AlinanSiparisTerminTakibi'])

@router.get('/', response_model=list[AlinanSiparisTerminTakibi])
async def list_alinan_siparis_termin_takibi(db: AsyncSession = Depends()):
    return await get_all_alinan_siparis_termin_takibi(db)

@router.get('/{id}', response_model=AlinanSiparisTerminTakibi)
async def get_alinan_siparis_termin_takibi_item(id: int, db: AsyncSession = Depends()):
    result = await get_alinan_siparis_termin_takibi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AlinanSiparisTerminTakibi)
async def create_alinan_siparis_termin_takibi_item(data: AlinanSiparisTerminTakibiCreate, db: AsyncSession = Depends()):
    db_item = DBAlinanSiparisTerminTakibi(**data.dict())
    return await create_alinan_siparis_termin_takibi(db, db_item)