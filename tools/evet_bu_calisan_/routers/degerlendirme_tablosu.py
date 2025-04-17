from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.degerlendirme_tablosu import DegerlendirmeTablosu, DegerlendirmeTablosuCreate
from models.degerlendirme_tablosu import DegerlendirmeTablosu as DBDegerlendirmeTablosu
from crud.degerlendirme_tablosu import get_all_degerlendirme_tablosu, get_degerlendirme_tablosu_by_id, create_degerlendirme_tablosu

router = APIRouter(prefix='/degerlendirme_tablosu', tags=['DegerlendirmeTablosu'])

@router.get('/', response_model=list[DegerlendirmeTablosu])
async def list_degerlendirme_tablosu(db: AsyncSession = Depends()):
    return await get_all_degerlendirme_tablosu(db)

@router.get('/{id}', response_model=DegerlendirmeTablosu)
async def get_degerlendirme_tablosu_item(id: int, db: AsyncSession = Depends()):
    result = await get_degerlendirme_tablosu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DegerlendirmeTablosu)
async def create_degerlendirme_tablosu_item(data: DegerlendirmeTablosuCreate, db: AsyncSession = Depends()):
    db_item = DBDegerlendirmeTablosu(**data.dict())
    return await create_degerlendirme_tablosu(db, db_item)