from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.dosya_malzeme import DosyaMalzeme, DosyaMalzemeCreate
from models.dosya_malzeme import DosyaMalzeme as DBDosyaMalzeme
from crud.dosya_malzeme import get_all_dosya_malzeme, get_dosya_malzeme_by_id, create_dosya_malzeme

router = APIRouter(prefix='/dosya_malzeme', tags=['DosyaMalzeme'])

@router.get('/', response_model=list[DosyaMalzeme])
async def list_dosya_malzeme(db: AsyncSession = Depends()):
    return await get_all_dosya_malzeme(db)

@router.get('/{id}', response_model=DosyaMalzeme)
async def get_dosya_malzeme_item(id: int, db: AsyncSession = Depends()):
    result = await get_dosya_malzeme_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DosyaMalzeme)
async def create_dosya_malzeme_item(data: DosyaMalzemeCreate, db: AsyncSession = Depends()):
    db_item = DBDosyaMalzeme(**data.dict())
    return await create_dosya_malzeme(db, db_item)