from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.ulke import Ulke, UlkeCreate
from models.ulke import Ulke as DBUlke
from crud.ulke import get_all_ulke, get_ulke_by_id, create_ulke

router = APIRouter(prefix='/ulke', tags=['Ulke'])

@router.get('/', response_model=list[Ulke])
async def list_ulke(db: AsyncSession = Depends()):
    return await get_all_ulke(db)

@router.get('/{id}', response_model=Ulke)
async def get_ulke_item(id: int, db: AsyncSession = Depends()):
    result = await get_ulke_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Ulke)
async def create_ulke_item(data: UlkeCreate, db: AsyncSession = Depends()):
    db_item = DBUlke(**data.dict())
    return await create_ulke(db, db_item)