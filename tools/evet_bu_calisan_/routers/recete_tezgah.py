from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete_tezgah import ReceteTezgah, ReceteTezgahCreate
from models.recete_tezgah import ReceteTezgah as DBReceteTezgah
from crud.recete_tezgah import get_all_recete_tezgah, get_recete_tezgah_by_id, create_recete_tezgah

router = APIRouter(prefix='/recete_tezgah', tags=['ReceteTezgah'])

@router.get('/', response_model=list[ReceteTezgah])
async def list_recete_tezgah(db: AsyncSession = Depends()):
    return await get_all_recete_tezgah(db)

@router.get('/{id}', response_model=ReceteTezgah)
async def get_recete_tezgah_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_tezgah_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ReceteTezgah)
async def create_recete_tezgah_item(data: ReceteTezgahCreate, db: AsyncSession = Depends()):
    db_item = DBReceteTezgah(**data.dict())
    return await create_recete_tezgah(db, db_item)