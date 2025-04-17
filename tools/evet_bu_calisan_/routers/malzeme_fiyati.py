from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_fiyati import MalzemeFiyati, MalzemeFiyatiCreate
from models.malzeme_fiyati import MalzemeFiyati as DBMalzemeFiyati
from crud.malzeme_fiyati import get_all_malzeme_fiyati, get_malzeme_fiyati_by_id, create_malzeme_fiyati

router = APIRouter(prefix='/malzeme_fiyati', tags=['MalzemeFiyati'])

@router.get('/', response_model=list[MalzemeFiyati])
async def list_malzeme_fiyati(db: AsyncSession = Depends()):
    return await get_all_malzeme_fiyati(db)

@router.get('/{id}', response_model=MalzemeFiyati)
async def get_malzeme_fiyati_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_fiyati_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeFiyati)
async def create_malzeme_fiyati_item(data: MalzemeFiyatiCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeFiyati(**data.dict())
    return await create_malzeme_fiyati(db, db_item)