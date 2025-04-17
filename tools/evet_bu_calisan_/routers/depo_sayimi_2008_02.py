from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2008_02 import DepoSayimi200802, DepoSayimi200802Create
from models.depo_sayimi_2008_02 import DepoSayimi200802 as DBDepoSayimi200802
from crud.depo_sayimi_2008_02 import get_all_depo_sayimi_2008_02, get_depo_sayimi_2008_02_by_id, create_depo_sayimi_2008_02

router = APIRouter(prefix='/depo_sayimi_2008_02', tags=['DepoSayimi200802'])

@router.get('/', response_model=list[DepoSayimi200802])
async def list_depo_sayimi_2008_02(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2008_02(db)

@router.get('/{id}', response_model=DepoSayimi200802)
async def get_depo_sayimi_2008_02_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2008_02_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi200802)
async def create_depo_sayimi_2008_02_item(data: DepoSayimi200802Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi200802(**data.dict())
    return await create_depo_sayimi_2008_02(db, db_item)