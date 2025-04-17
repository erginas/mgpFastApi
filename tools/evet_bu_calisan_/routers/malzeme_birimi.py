from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_birimi import MalzemeBirimi, MalzemeBirimiCreate
from models.malzeme_birimi import MalzemeBirimi as DBMalzemeBirimi
from crud.malzeme_birimi import get_all_malzeme_birimi, get_malzeme_birimi_by_id, create_malzeme_birimi

router = APIRouter(prefix='/malzeme_birimi', tags=['MalzemeBirimi'])

@router.get('/', response_model=list[MalzemeBirimi])
async def list_malzeme_birimi(db: AsyncSession = Depends()):
    return await get_all_malzeme_birimi(db)

@router.get('/{id}', response_model=MalzemeBirimi)
async def get_malzeme_birimi_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_birimi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeBirimi)
async def create_malzeme_birimi_item(data: MalzemeBirimiCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeBirimi(**data.dict())
    return await create_malzeme_birimi(db, db_item)