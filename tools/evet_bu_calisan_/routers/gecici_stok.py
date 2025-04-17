from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.gecici_stok import GeciciStok, GeciciStokCreate
from models.gecici_stok import GeciciStok as DBGeciciStok
from crud.gecici_stok import get_all_gecici_stok, get_gecici_stok_by_id, create_gecici_stok

router = APIRouter(prefix='/gecici_stok', tags=['GeciciStok'])

@router.get('/', response_model=list[GeciciStok])
async def list_gecici_stok(db: AsyncSession = Depends()):
    return await get_all_gecici_stok(db)

@router.get('/{id}', response_model=GeciciStok)
async def get_gecici_stok_item(id: int, db: AsyncSession = Depends()):
    result = await get_gecici_stok_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=GeciciStok)
async def create_gecici_stok_item(data: GeciciStokCreate, db: AsyncSession = Depends()):
    db_item = DBGeciciStok(**data.dict())
    return await create_gecici_stok(db, db_item)