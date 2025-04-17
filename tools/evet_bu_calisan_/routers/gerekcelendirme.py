from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.gerekcelendirme import Gerekcelendirme, GerekcelendirmeCreate
from models.gerekcelendirme import Gerekcelendirme as DBGerekcelendirme
from crud.gerekcelendirme import get_all_gerekcelendirme, get_gerekcelendirme_by_id, create_gerekcelendirme

router = APIRouter(prefix='/gerekcelendirme', tags=['Gerekcelendirme'])

@router.get('/', response_model=list[Gerekcelendirme])
async def list_gerekcelendirme(db: AsyncSession = Depends()):
    return await get_all_gerekcelendirme(db)

@router.get('/{id}', response_model=Gerekcelendirme)
async def get_gerekcelendirme_item(id: int, db: AsyncSession = Depends()):
    result = await get_gerekcelendirme_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Gerekcelendirme)
async def create_gerekcelendirme_item(data: GerekcelendirmeCreate, db: AsyncSession = Depends()):
    db_item = DBGerekcelendirme(**data.dict())
    return await create_gerekcelendirme(db, db_item)