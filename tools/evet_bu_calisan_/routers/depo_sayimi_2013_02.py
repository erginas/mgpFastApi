from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2013_02 import DepoSayimi201302, DepoSayimi201302Create
from models.depo_sayimi_2013_02 import DepoSayimi201302 as DBDepoSayimi201302
from crud.depo_sayimi_2013_02 import get_all_depo_sayimi_2013_02, get_depo_sayimi_2013_02_by_id, create_depo_sayimi_2013_02

router = APIRouter(prefix='/depo_sayimi_2013_02', tags=['DepoSayimi201302'])

@router.get('/', response_model=list[DepoSayimi201302])
async def list_depo_sayimi_2013_02(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2013_02(db)

@router.get('/{id}', response_model=DepoSayimi201302)
async def get_depo_sayimi_2013_02_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2013_02_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi201302)
async def create_depo_sayimi_2013_02_item(data: DepoSayimi201302Create, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi201302(**data.dict())
    return await create_depo_sayimi_2013_02(db, db_item)