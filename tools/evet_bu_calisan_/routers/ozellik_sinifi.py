from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.ozellik_sinifi import OzellikSinifi, OzellikSinifiCreate
from models.ozellik_sinifi import OzellikSinifi as DBOzellikSinifi
from crud.ozellik_sinifi import get_all_ozellik_sinifi, get_ozellik_sinifi_by_id, create_ozellik_sinifi

router = APIRouter(prefix='/ozellik_sinifi', tags=['OzellikSinifi'])

@router.get('/', response_model=list[OzellikSinifi])
async def list_ozellik_sinifi(db: AsyncSession = Depends()):
    return await get_all_ozellik_sinifi(db)

@router.get('/{id}', response_model=OzellikSinifi)
async def get_ozellik_sinifi_item(id: int, db: AsyncSession = Depends()):
    result = await get_ozellik_sinifi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=OzellikSinifi)
async def create_ozellik_sinifi_item(data: OzellikSinifiCreate, db: AsyncSession = Depends()):
    db_item = DBOzellikSinifi(**data.dict())
    return await create_ozellik_sinifi(db, db_item)