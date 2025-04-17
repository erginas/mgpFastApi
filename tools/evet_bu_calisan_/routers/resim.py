from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.resim import Resim, ResimCreate
from models.resim import Resim as DBResim
from crud.resim import get_all_resim, get_resim_by_id, create_resim

router = APIRouter(prefix='/resim', tags=['Resim'])

@router.get('/', response_model=list[Resim])
async def list_resim(db: AsyncSession = Depends()):
    return await get_all_resim(db)

@router.get('/{id}', response_model=Resim)
async def get_resim_item(id: int, db: AsyncSession = Depends()):
    result = await get_resim_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Resim)
async def create_resim_item(data: ResimCreate, db: AsyncSession = Depends()):
    db_item = DBResim(**data.dict())
    return await create_resim(db, db_item)