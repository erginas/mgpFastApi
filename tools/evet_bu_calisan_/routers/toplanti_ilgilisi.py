from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.toplanti_ilgilisi import ToplantiIlgilisi, ToplantiIlgilisiCreate
from models.toplanti_ilgilisi import ToplantiIlgilisi as DBToplantiIlgilisi
from crud.toplanti_ilgilisi import get_all_toplanti_ilgilisi, get_toplanti_ilgilisi_by_id, create_toplanti_ilgilisi

router = APIRouter(prefix='/toplanti_ilgilisi', tags=['ToplantiIlgilisi'])

@router.get('/', response_model=list[ToplantiIlgilisi])
async def list_toplanti_ilgilisi(db: AsyncSession = Depends()):
    return await get_all_toplanti_ilgilisi(db)

@router.get('/{id}', response_model=ToplantiIlgilisi)
async def get_toplanti_ilgilisi_item(id: int, db: AsyncSession = Depends()):
    result = await get_toplanti_ilgilisi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ToplantiIlgilisi)
async def create_toplanti_ilgilisi_item(data: ToplantiIlgilisiCreate, db: AsyncSession = Depends()):
    db_item = DBToplantiIlgilisi(**data.dict())
    return await create_toplanti_ilgilisi(db, db_item)