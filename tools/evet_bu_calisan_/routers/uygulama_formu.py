from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uygulama_formu import UygulamaFormu, UygulamaFormuCreate
from models.uygulama_formu import UygulamaFormu as DBUygulamaFormu
from crud.uygulama_formu import get_all_uygulama_formu, get_uygulama_formu_by_id, create_uygulama_formu

router = APIRouter(prefix='/uygulama_formu', tags=['UygulamaFormu'])

@router.get('/', response_model=list[UygulamaFormu])
async def list_uygulama_formu(db: AsyncSession = Depends()):
    return await get_all_uygulama_formu(db)

@router.get('/{id}', response_model=UygulamaFormu)
async def get_uygulama_formu_item(id: int, db: AsyncSession = Depends()):
    result = await get_uygulama_formu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UygulamaFormu)
async def create_uygulama_formu_item(data: UygulamaFormuCreate, db: AsyncSession = Depends()):
    db_item = DBUygulamaFormu(**data.dict())
    return await create_uygulama_formu(db, db_item)