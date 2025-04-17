from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uts_baslik import UtsBaslik, UtsBaslikCreate
from models.uts_baslik import UtsBaslik as DBUtsBaslik
from crud.uts_baslik import get_all_uts_baslik, get_uts_baslik_by_id, create_uts_baslik

router = APIRouter(prefix='/uts_baslik', tags=['UtsBaslik'])

@router.get('/', response_model=list[UtsBaslik])
async def list_uts_baslik(db: AsyncSession = Depends()):
    return await get_all_uts_baslik(db)

@router.get('/{id}', response_model=UtsBaslik)
async def get_uts_baslik_item(id: int, db: AsyncSession = Depends()):
    result = await get_uts_baslik_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UtsBaslik)
async def create_uts_baslik_item(data: UtsBaslikCreate, db: AsyncSession = Depends()):
    db_item = DBUtsBaslik(**data.dict())
    return await create_uts_baslik(db, db_item)