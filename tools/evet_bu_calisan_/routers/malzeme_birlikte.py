from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_birlikte import MalzemeBirlikte, MalzemeBirlikteCreate
from models.malzeme_birlikte import MalzemeBirlikte as DBMalzemeBirlikte
from crud.malzeme_birlikte import get_all_malzeme_birlikte, get_malzeme_birlikte_by_id, create_malzeme_birlikte

router = APIRouter(prefix='/malzeme_birlikte', tags=['MalzemeBirlikte'])

@router.get('/', response_model=list[MalzemeBirlikte])
async def list_malzeme_birlikte(db: AsyncSession = Depends()):
    return await get_all_malzeme_birlikte(db)

@router.get('/{id}', response_model=MalzemeBirlikte)
async def get_malzeme_birlikte_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_birlikte_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeBirlikte)
async def create_malzeme_birlikte_item(data: MalzemeBirlikteCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeBirlikte(**data.dict())
    return await create_malzeme_birlikte(db, db_item)