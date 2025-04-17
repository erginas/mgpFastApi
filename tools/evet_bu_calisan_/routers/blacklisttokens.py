from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.blacklisttokens import Blacklisttokens, BlacklisttokensCreate
from models.blacklisttokens import Blacklisttokens as DBBlacklisttokens
from crud.blacklisttokens import get_all_blacklisttokens, get_blacklisttokens_by_id, create_blacklisttokens

router = APIRouter(prefix='/blacklisttokens', tags=['Blacklisttokens'])

@router.get('/', response_model=list[Blacklisttokens])
async def list_blacklisttokens(db: AsyncSession = Depends()):
    return await get_all_blacklisttokens(db)

@router.get('/{id}', response_model=Blacklisttokens)
async def get_blacklisttokens_item(id: int, db: AsyncSession = Depends()):
    result = await get_blacklisttokens_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Blacklisttokens)
async def create_blacklisttokens_item(data: BlacklisttokensCreate, db: AsyncSession = Depends()):
    db_item = DBBlacklisttokens(**data.dict())
    return await create_blacklisttokens(db, db_item)