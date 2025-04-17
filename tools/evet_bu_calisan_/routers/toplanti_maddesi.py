from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.toplanti_maddesi import ToplantiMaddesi, ToplantiMaddesiCreate
from models.toplanti_maddesi import ToplantiMaddesi as DBToplantiMaddesi
from crud.toplanti_maddesi import get_all_toplanti_maddesi, get_toplanti_maddesi_by_id, create_toplanti_maddesi

router = APIRouter(prefix='/toplanti_maddesi', tags=['ToplantiMaddesi'])

@router.get('/', response_model=list[ToplantiMaddesi])
async def list_toplanti_maddesi(db: AsyncSession = Depends()):
    return await get_all_toplanti_maddesi(db)

@router.get('/{id}', response_model=ToplantiMaddesi)
async def get_toplanti_maddesi_item(id: int, db: AsyncSession = Depends()):
    result = await get_toplanti_maddesi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=ToplantiMaddesi)
async def create_toplanti_maddesi_item(data: ToplantiMaddesiCreate, db: AsyncSession = Depends()):
    db_item = DBToplantiMaddesi(**data.dict())
    return await create_toplanti_maddesi(db, db_item)