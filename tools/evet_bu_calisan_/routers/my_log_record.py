from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.my_log_record import MyLogRecord, MyLogRecordCreate
from models.my_log_record import MyLogRecord as DBMyLogRecord
from crud.my_log_record import get_all_my_log_record, get_my_log_record_by_id, create_my_log_record

router = APIRouter(prefix='/my_log_record', tags=['MyLogRecord'])

@router.get('/', response_model=list[MyLogRecord])
async def list_my_log_record(db: AsyncSession = Depends()):
    return await get_all_my_log_record(db)

@router.get('/{id}', response_model=MyLogRecord)
async def get_my_log_record_item(id: int, db: AsyncSession = Depends()):
    result = await get_my_log_record_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MyLogRecord)
async def create_my_log_record_item(data: MyLogRecordCreate, db: AsyncSession = Depends()):
    db_item = DBMyLogRecord(**data.dict())
    return await create_my_log_record(db, db_item)