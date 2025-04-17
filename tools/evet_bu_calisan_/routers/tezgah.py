from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tezgah import Tezgah, TezgahCreate
from models.tezgah import Tezgah as DBTezgah
from crud.tezgah import get_all_tezgah, get_tezgah_by_id, create_tezgah

router = APIRouter(prefix='/tezgah', tags=['Tezgah'])

@router.get('/', response_model=list[Tezgah])
async def list_tezgah(db: AsyncSession = Depends()):
    return await get_all_tezgah(db)

@router.get('/{id}', response_model=Tezgah)
async def get_tezgah_item(id: int, db: AsyncSession = Depends()):
    result = await get_tezgah_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Tezgah)
async def create_tezgah_item(data: TezgahCreate, db: AsyncSession = Depends()):
    db_item = DBTezgah(**data.dict())
    return await create_tezgah(db, db_item)