from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.degerlendirme_kriteri import DegerlendirmeKriteri, DegerlendirmeKriteriCreate
from models.degerlendirme_kriteri import DegerlendirmeKriteri as DBDegerlendirmeKriteri
from crud.degerlendirme_kriteri import get_all_degerlendirme_kriteri, get_degerlendirme_kriteri_by_id, create_degerlendirme_kriteri

router = APIRouter(prefix='/degerlendirme_kriteri', tags=['DegerlendirmeKriteri'])

@router.get('/', response_model=list[DegerlendirmeKriteri])
async def list_degerlendirme_kriteri(db: AsyncSession = Depends()):
    return await get_all_degerlendirme_kriteri(db)

@router.get('/{id}', response_model=DegerlendirmeKriteri)
async def get_degerlendirme_kriteri_item(id: int, db: AsyncSession = Depends()):
    result = await get_degerlendirme_kriteri_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DegerlendirmeKriteri)
async def create_degerlendirme_kriteri_item(data: DegerlendirmeKriteriCreate, db: AsyncSession = Depends()):
    db_item = DBDegerlendirmeKriteri(**data.dict())
    return await create_degerlendirme_kriteri(db, db_item)