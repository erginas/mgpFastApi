from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme import Malzeme, MalzemeCreate
from models.malzeme import Malzeme as DBMalzeme
from crud.malzeme import get_all_malzeme, get_malzeme_by_id, create_malzeme

router = APIRouter(prefix='/malzeme', tags=['Malzeme'])

@router.get('/', response_model=list[Malzeme])
async def list_malzeme(db: AsyncSession = Depends()):
    return await get_all_malzeme(db)

@router.get('/{id}', response_model=Malzeme)
async def get_malzeme_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Malzeme)
async def create_malzeme_item(data: MalzemeCreate, db: AsyncSession = Depends()):
    db_item = DBMalzeme(**data.dict())
    return await create_malzeme(db, db_item)