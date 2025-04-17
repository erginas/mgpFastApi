from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.ozellik_sablonu import OzellikSablonu, OzellikSablonuCreate
from models.ozellik_sablonu import OzellikSablonu as DBOzellikSablonu
from crud.ozellik_sablonu import get_all_ozellik_sablonu, get_ozellik_sablonu_by_id, create_ozellik_sablonu

router = APIRouter(prefix='/ozellik_sablonu', tags=['OzellikSablonu'])

@router.get('/', response_model=list[OzellikSablonu])
async def list_ozellik_sablonu(db: AsyncSession = Depends()):
    return await get_all_ozellik_sablonu(db)

@router.get('/{id}', response_model=OzellikSablonu)
async def get_ozellik_sablonu_item(id: int, db: AsyncSession = Depends()):
    result = await get_ozellik_sablonu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=OzellikSablonu)
async def create_ozellik_sablonu_item(data: OzellikSablonuCreate, db: AsyncSession = Depends()):
    db_item = DBOzellikSablonu(**data.dict())
    return await create_ozellik_sablonu(db, db_item)