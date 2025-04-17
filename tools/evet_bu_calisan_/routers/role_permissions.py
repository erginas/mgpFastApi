from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.role_permissions import RolePermissions, RolePermissionsCreate
from models.role_permissions import RolePermissions as DBRolePermissions
from crud.role_permissions import get_all_role_permissions, get_role_permissions_by_id, create_role_permissions

router = APIRouter(prefix='/role_permissions', tags=['RolePermissions'])

@router.get('/', response_model=list[RolePermissions])
async def list_role_permissions(db: AsyncSession = Depends()):
    return await get_all_role_permissions(db)

@router.get('/{id}', response_model=RolePermissions)
async def get_role_permissions_item(id: int, db: AsyncSession = Depends()):
    result = await get_role_permissions_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=RolePermissions)
async def create_role_permissions_item(data: RolePermissionsCreate, db: AsyncSession = Depends()):
    db_item = DBRolePermissions(**data.dict())
    return await create_role_permissions(db, db_item)