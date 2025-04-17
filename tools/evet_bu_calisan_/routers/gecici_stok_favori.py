from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.gecici_stok_favori import GeciciStokFavori, GeciciStokFavoriCreate
from models.gecici_stok_favori import GeciciStokFavori as DBGeciciStokFavori
from crud.gecici_stok_favori import get_all_gecici_stok_favori, get_gecici_stok_favori_by_id, create_gecici_stok_favori

router = APIRouter(prefix='/gecici_stok_favori', tags=['GeciciStokFavori'])

@router.get('/', response_model=list[GeciciStokFavori])
async def list_gecici_stok_favori(db: AsyncSession = Depends()):
    return await get_all_gecici_stok_favori(db)

@router.get('/{id}', response_model=GeciciStokFavori)
async def get_gecici_stok_favori_item(id: int, db: AsyncSession = Depends()):
    result = await get_gecici_stok_favori_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=GeciciStokFavori)
async def create_gecici_stok_favori_item(data: GeciciStokFavoriCreate, db: AsyncSession = Depends()):
    db_item = DBGeciciStokFavori(**data.dict())
    return await create_gecici_stok_favori(db, db_item)