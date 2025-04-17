from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kontrol_prefix import KontrolPrefix, KontrolPrefixCreate
from models.kontrol_prefix import KontrolPrefix as DBKontrolPrefix
from crud.kontrol_prefix import get_all_kontrol_prefix, get_kontrol_prefix_by_id, create_kontrol_prefix

router = APIRouter(prefix='/kontrol_prefix', tags=['KontrolPrefix'])

@router.get('/', response_model=list[KontrolPrefix])
async def list_kontrol_prefix(db: AsyncSession = Depends()):
    return await get_all_kontrol_prefix(db)

@router.get('/{id}', response_model=KontrolPrefix)
async def get_kontrol_prefix_item(id: int, db: AsyncSession = Depends()):
    result = await get_kontrol_prefix_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=KontrolPrefix)
async def create_kontrol_prefix_item(data: KontrolPrefixCreate, db: AsyncSession = Depends()):
    db_item = DBKontrolPrefix(**data.dict())
    return await create_kontrol_prefix(db, db_item)