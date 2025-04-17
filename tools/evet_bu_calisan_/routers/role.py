from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.role import Role, RoleCreate
from models.role import Role as DBRole
from crud.role import get_all_role, get_role_by_id, create_role

router = APIRouter(prefix='/role', tags=['Role'])

@router.get('/', response_model=list[Role])
async def list_role(db: AsyncSession = Depends()):
    return await get_all_role(db)

@router.get('/{id}', response_model=Role)
async def get_role_item(id: int, db: AsyncSession = Depends()):
    result = await get_role_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Role)
async def create_role_item(data: RoleCreate, db: AsyncSession = Depends()):
    db_item = DBRole(**data.dict())
    return await create_role(db, db_item)