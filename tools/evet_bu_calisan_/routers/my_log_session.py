from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.my_log_session import MyLogSession, MyLogSessionCreate
from models.my_log_session import MyLogSession as DBMyLogSession
from crud.my_log_session import get_all_my_log_session, get_my_log_session_by_id, create_my_log_session

router = APIRouter(prefix='/my_log_session', tags=['MyLogSession'])

@router.get('/', response_model=list[MyLogSession])
async def list_my_log_session(db: AsyncSession = Depends()):
    return await get_all_my_log_session(db)

@router.get('/{id}', response_model=MyLogSession)
async def get_my_log_session_item(id: int, db: AsyncSession = Depends()):
    result = await get_my_log_session_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MyLogSession)
async def create_my_log_session_item(data: MyLogSessionCreate, db: AsyncSession = Depends()):
    db_item = DBMyLogSession(**data.dict())
    return await create_my_log_session(db, db_item)