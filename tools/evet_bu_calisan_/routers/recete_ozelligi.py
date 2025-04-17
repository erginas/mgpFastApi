from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.recete_ozelligi import ReceteOzelligi, ReceteOzelligiCreate
from models.recete_ozelligi import ReceteOzelligi as DBReceteOzelligi
from crud.recete_ozelligi import get_all_recete_ozelligi, get_recete_ozelligi_by_id, create_recete_ozelligi

router = APIRouter(prefix='/recete_ozelligi', tags=['ReceteOzelligi'])

@router.get('/', response_model=list[ReceteOzelligi])
async def list_recete_ozelligi(db: AsyncSession = Depends()):
    return await get_all_recete_ozelligi(db)

@router.get('/{id}', response_model=ReceteOzelligi)
async def get_recete_ozelligi_item(id: int, db: AsyncSession = Depends()):
    result = await get_recete_ozelligi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ReceteOzelligi)
async def create_recete_ozelligi_item(data: ReceteOzelligiCreate, db: AsyncSession = Depends()):
    db_item = DBReceteOzelligi(**data.dict())
    return await create_recete_ozelligi(db, db_item)