from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.permission import Permission, PermissionCreate
from models.permission import Permission as DBPermission
from crud.permission import get_all_permission, get_permission_by_id, create_permission

router = APIRouter(prefix='/permission', tags=['Permission'])

@router.get('/', response_model=list[Permission])
async def list_permission(db: AsyncSession = Depends()):
    return await get_all_permission(db)

@router.get('/{id}', response_model=Permission)
async def get_permission_item(id: int, db: AsyncSession = Depends()):
    result = await get_permission_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Permission)
async def create_permission_item(data: PermissionCreate, db: AsyncSession = Depends()):
    db_item = DBPermission(**data.dict())
    return await create_permission(db, db_item)