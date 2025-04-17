from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete_sinifi import ReceteSinifi, ReceteSinifiCreate
from models.recete_sinifi import ReceteSinifi as DBReceteSinifi
from crud.recete_sinifi import get_all_recete_sinifi, get_recete_sinifi_by_id, create_recete_sinifi

router = APIRouter(prefix='/recete_sinifi', tags=['ReceteSinifi'])

@router.get('/', response_model=list[ReceteSinifi])
async def list_recete_sinifi(db: AsyncSession = Depends()):
    return await get_all_recete_sinifi(db)

@router.get('/{id}', response_model=ReceteSinifi)
async def get_recete_sinifi_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_sinifi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ReceteSinifi)
async def create_recete_sinifi_item(data: ReceteSinifiCreate, db: AsyncSession = Depends()):
    db_item = DBReceteSinifi(**data.dict())
    return await create_recete_sinifi(db, db_item)