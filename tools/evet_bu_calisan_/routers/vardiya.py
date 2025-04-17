from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.vardiya import Vardiya, VardiyaCreate
from models.vardiya import Vardiya as DBVardiya
from crud.vardiya import get_all_vardiya, get_vardiya_by_id, create_vardiya

router = APIRouter(prefix='/vardiya', tags=['Vardiya'])

@router.get('/', response_model=list[Vardiya])
async def list_vardiya(db: AsyncSession = Depends()):
    return await get_all_vardiya(db)

@router.get('/{id}', response_model=Vardiya)
async def get_vardiya_item(id: int, db: AsyncSession = Depends()):
    result = await get_vardiya_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Vardiya)
async def create_vardiya_item(data: VardiyaCreate, db: AsyncSession = Depends()):
    db_item = DBVardiya(**data.dict())
    return await create_vardiya(db, db_item)