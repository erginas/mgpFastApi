from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete_malzeme import ReceteMalzeme, ReceteMalzemeCreate
from models.recete_malzeme import ReceteMalzeme as DBReceteMalzeme
from crud.recete_malzeme import get_all_recete_malzeme, get_recete_malzeme_by_id, create_recete_malzeme

router = APIRouter(prefix='/recete_malzeme', tags=['ReceteMalzeme'])

@router.get('/', response_model=list[ReceteMalzeme])
async def list_recete_malzeme(db: AsyncSession = Depends()):
    return await get_all_recete_malzeme(db)

@router.get('/{id}', response_model=ReceteMalzeme)
async def get_recete_malzeme_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_malzeme_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ReceteMalzeme)
async def create_recete_malzeme_item(data: ReceteMalzemeCreate, db: AsyncSession = Depends()):
    db_item = DBReceteMalzeme(**data.dict())
    return await create_recete_malzeme(db, db_item)