from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.aktarma import Aktarma, AktarmaCreate
from models.aktarma import Aktarma as DBAktarma
from crud.aktarma import get_all_aktarma, get_aktarma_by_id, create_aktarma

router = APIRouter(prefix='/aktarma', tags=['Aktarma'])

@router.get('/', response_model=list[Aktarma])
async def list_aktarma(db: AsyncSession = Depends()):
    return await get_all_aktarma(db)

@router.get('/{id}', response_model=Aktarma)
async def get_aktarma_item(id: int, db: AsyncSession = Depends()):
    result = await get_aktarma_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Aktarma)
async def create_aktarma_item(data: AktarmaCreate, db: AsyncSession = Depends()):
    db_item = DBAktarma(**data.dict())
    return await create_aktarma(db, db_item)