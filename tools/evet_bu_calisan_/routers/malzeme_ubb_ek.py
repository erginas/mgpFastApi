from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_ubb_ek import MalzemeUbbEk, MalzemeUbbEkCreate
from models.malzeme_ubb_ek import MalzemeUbbEk as DBMalzemeUbbEk
from crud.malzeme_ubb_ek import get_all_malzeme_ubb_ek, get_malzeme_ubb_ek_by_id, create_malzeme_ubb_ek

router = APIRouter(prefix='/malzeme_ubb_ek', tags=['MalzemeUbbEk'])

@router.get('/', response_model=list[MalzemeUbbEk])
async def list_malzeme_ubb_ek(db: AsyncSession = Depends()):
    return await get_all_malzeme_ubb_ek(db)

@router.get('/{id}', response_model=MalzemeUbbEk)
async def get_malzeme_ubb_ek_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_ubb_ek_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeUbbEk)
async def create_malzeme_ubb_ek_item(data: MalzemeUbbEkCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeUbbEk(**data.dict())
    return await create_malzeme_ubb_ek(db, db_item)