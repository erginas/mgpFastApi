from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.uts_temp import UtsTemp, UtsTempCreate
from models.uts_temp import UtsTemp as DBUtsTemp
from crud.uts_temp import get_all_uts_temp, get_uts_temp_by_id, create_uts_temp

router = APIRouter(prefix='/uts_temp', tags=['UtsTemp'])

@router.get('/', response_model=list[UtsTemp])
async def list_uts_temp(db: AsyncSession = Depends()):
    return await get_all_uts_temp(db)

@router.get('/{id}', response_model=UtsTemp)
async def get_uts_temp_item(id: int, db: AsyncSession = Depends()):
    result = await get_uts_temp_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=UtsTemp)
async def create_uts_temp_item(data: UtsTempCreate, db: AsyncSession = Depends()):
    db_item = DBUtsTemp(**data.dict())
    return await create_uts_temp(db, db_item)