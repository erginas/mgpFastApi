from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_ozelligi import MalzemeOzelligi, MalzemeOzelligiCreate
from models.malzeme_ozelligi import MalzemeOzelligi as DBMalzemeOzelligi
from crud.malzeme_ozelligi import get_all_malzeme_ozelligi, get_malzeme_ozelligi_by_id, create_malzeme_ozelligi

router = APIRouter(prefix='/malzeme_ozelligi', tags=['MalzemeOzelligi'])

@router.get('/', response_model=list[MalzemeOzelligi])
async def list_malzeme_ozelligi(db: AsyncSession = Depends()):
    return await get_all_malzeme_ozelligi(db)

@router.get('/{id}', response_model=MalzemeOzelligi)
async def get_malzeme_ozelligi_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_ozelligi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeOzelligi)
async def create_malzeme_ozelligi_item(data: MalzemeOzelligiCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeOzelligi(**data.dict())
    return await create_malzeme_ozelligi(db, db_item)