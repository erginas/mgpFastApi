from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.users import Users, UsersCreate
from models.users import Users as DBUsers
from crud.users import get_all_users, get_users_by_id, create_users

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/', response_model=list[Users])
async def list_users(db: AsyncSession = Depends()):
    return await get_all_users(db)

@router.get('/{id}', response_model=Users)
async def get_users_item(id: int, db: AsyncSession = Depends()):
    result = await get_users_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Users)
async def create_users_item(data: UsersCreate, db: AsyncSession = Depends()):
    db_item = DBUsers(**data.dict())
    return await create_users(db, db_item)