from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.resim_olcusu import ResimOlcusu, ResimOlcusuCreate
from models.resim_olcusu import ResimOlcusu as DBResimOlcusu
from crud.resim_olcusu import get_all_resim_olcusu, get_resim_olcusu_by_id, create_resim_olcusu

router = APIRouter(prefix='/resim_olcusu', tags=['ResimOlcusu'])

@router.get('/', response_model=list[ResimOlcusu])
async def list_resim_olcusu(db: AsyncSession = Depends()):
    return await get_all_resim_olcusu(db)

@router.get('/{id}', response_model=ResimOlcusu)
async def get_resim_olcusu_item(id: int, db: AsyncSession = Depends()):
    result = await get_resim_olcusu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ResimOlcusu)
async def create_resim_olcusu_item(data: ResimOlcusuCreate, db: AsyncSession = Depends()):
    db_item = DBResimOlcusu(**data.dict())
    return await create_resim_olcusu(db, db_item)