from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.banka_hesabi import BankaHesabi, BankaHesabiCreate
from models.banka_hesabi import BankaHesabi as DBBankaHesabi
from crud.banka_hesabi import get_all_banka_hesabi, get_banka_hesabi_by_id, create_banka_hesabi

router = APIRouter(prefix='/banka_hesabi', tags=['BankaHesabi'])

@router.get('/', response_model=list[BankaHesabi])
async def list_banka_hesabi(db: AsyncSession = Depends()):
    return await get_all_banka_hesabi(db)

@router.get('/{id}', response_model=BankaHesabi)
async def get_banka_hesabi_item(id: int, db: AsyncSession = Depends()):
    result = await get_banka_hesabi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=BankaHesabi)
async def create_banka_hesabi_item(data: BankaHesabiCreate, db: AsyncSession = Depends()):
    db_item = DBBankaHesabi(**data.dict())
    return await create_banka_hesabi(db, db_item)