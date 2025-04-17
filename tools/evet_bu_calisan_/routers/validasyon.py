from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.validasyon import Validasyon, ValidasyonCreate
from models.validasyon import Validasyon as DBValidasyon
from crud.validasyon import get_all_validasyon, get_validasyon_by_id, create_validasyon

router = APIRouter(prefix='/validasyon', tags=['Validasyon'])

@router.get('/', response_model=list[Validasyon])
async def list_validasyon(db: AsyncSession = Depends()):
    return await get_all_validasyon(db)

@router.get('/{id}', response_model=Validasyon)
async def get_validasyon_item(id: int, db: AsyncSession = Depends()):
    result = await get_validasyon_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Validasyon)
async def create_validasyon_item(data: ValidasyonCreate, db: AsyncSession = Depends()):
    db_item = DBValidasyon(**data.dict())
    return await create_validasyon(db, db_item)