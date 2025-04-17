from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.ubb_transfer import UbbTransfer, UbbTransferCreate
from models.ubb_transfer import UbbTransfer as DBUbbTransfer
from crud.ubb_transfer import get_all_ubb_transfer, get_ubb_transfer_by_id, create_ubb_transfer

router = APIRouter(prefix='/ubb_transfer', tags=['UbbTransfer'])

@router.get('/', response_model=list[UbbTransfer])
async def list_ubb_transfer(db: AsyncSession = Depends()):
    return await get_all_ubb_transfer(db)

@router.get('/{id}', response_model=UbbTransfer)
async def get_ubb_transfer_item(id: int, db: AsyncSession = Depends()):
    result = await get_ubb_transfer_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UbbTransfer)
async def create_ubb_transfer_item(data: UbbTransferCreate, db: AsyncSession = Depends()):
    db_item = DBUbbTransfer(**data.dict())
    return await create_ubb_transfer(db, db_item)