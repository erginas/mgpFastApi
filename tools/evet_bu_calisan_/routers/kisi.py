from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kisi import Kisi, KisiCreate
from models.kisi import Kisi as DBKisi
from crud.kisi import get_all_kisi, get_kisi_by_id, create_kisi

router = APIRouter(prefix='/kisi', tags=['Kisi'])

@router.get('/', response_model=list[Kisi])
async def list_kisi(db: AsyncSession = Depends()):
    return await get_all_kisi(db)

@router.get('/{id}', response_model=Kisi)
async def get_kisi_item(id: int, db: AsyncSession = Depends()):
    result = await get_kisi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Kisi)
async def create_kisi_item(data: KisiCreate, db: AsyncSession = Depends()):
    db_item = DBKisi(**data.dict())
    return await create_kisi(db, db_item)