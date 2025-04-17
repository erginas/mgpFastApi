from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.my_log_value import MyLogValue, MyLogValueCreate
from models.my_log_value import MyLogValue as DBMyLogValue
from crud.my_log_value import get_all_my_log_value, get_my_log_value_by_id, create_my_log_value

router = APIRouter(prefix='/my_log_value', tags=['MyLogValue'])

@router.get('/', response_model=list[MyLogValue])
async def list_my_log_value(db: AsyncSession = Depends()):
    return await get_all_my_log_value(db)

@router.get('/{id}', response_model=MyLogValue)
async def get_my_log_value_item(id: int, db: AsyncSession = Depends()):
    result = await get_my_log_value_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MyLogValue)
async def create_my_log_value_item(data: MyLogValueCreate, db: AsyncSession = Depends()):
    db_item = DBMyLogValue(**data.dict())
    return await create_my_log_value(db, db_item)