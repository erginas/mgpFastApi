from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_set import MalzemeSet, MalzemeSetCreate
from models.malzeme_set import MalzemeSet as DBMalzemeSet
from crud.malzeme_set import get_all_malzeme_set, get_malzeme_set_by_id, create_malzeme_set

router = APIRouter(prefix='/malzeme_set', tags=['MalzemeSet'])

@router.get('/', response_model=list[MalzemeSet])
async def list_malzeme_set(db: AsyncSession = Depends()):
    return await get_all_malzeme_set(db)

@router.get('/{id}', response_model=MalzemeSet)
async def get_malzeme_set_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_set_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeSet)
async def create_malzeme_set_item(data: MalzemeSetCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeSet(**data.dict())
    return await create_malzeme_set(db, db_item)