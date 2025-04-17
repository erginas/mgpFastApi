from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_plani import MalzemePlani, MalzemePlaniCreate
from models.malzeme_plani import MalzemePlani as DBMalzemePlani
from crud.malzeme_plani import get_all_malzeme_plani, get_malzeme_plani_by_id, create_malzeme_plani

router = APIRouter(prefix='/malzeme_plani', tags=['MalzemePlani'])

@router.get('/', response_model=list[MalzemePlani])
async def list_malzeme_plani(db: AsyncSession = Depends()):
    return await get_all_malzeme_plani(db)

@router.get('/{id}', response_model=MalzemePlani)
async def get_malzeme_plani_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_plani_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemePlani)
async def create_malzeme_plani_item(data: MalzemePlaniCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemePlani(**data.dict())
    return await create_malzeme_plani(db, db_item)