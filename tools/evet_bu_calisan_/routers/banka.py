from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.banka import Banka, BankaCreate
from models.banka import Banka as DBBanka
from crud.banka import get_all_banka, get_banka_by_id, create_banka

router = APIRouter(prefix='/banka', tags=['Banka'])

@router.get('/', response_model=list[Banka])
async def list_banka(db: AsyncSession = Depends()):
    return await get_all_banka(db)

@router.get('/{id}', response_model=Banka)
async def get_banka_item(id: int, db: AsyncSession = Depends()):
    result = await get_banka_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Banka)
async def create_banka_item(data: BankaCreate, db: AsyncSession = Depends()):
    db_item = DBBanka(**data.dict())
    return await create_banka(db, db_item)