from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.alembic_version import AlembicVersion, AlembicVersionCreate
from models.alembic_version import AlembicVersion as DBAlembicVersion
from crud.alembic_version import get_all_alembic_version, get_alembic_version_by_id, create_alembic_version

router = APIRouter(prefix='/alembic_version', tags=['AlembicVersion'])

@router.get('/', response_model=list[AlembicVersion])
async def list_alembic_version(db: AsyncSession = Depends()):
    return await get_all_alembic_version(db)

@router.get('/{id}', response_model=AlembicVersion)
async def get_alembic_version_item(id: int, db: AsyncSession = Depends()):
    result = await get_alembic_version_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AlembicVersion)
async def create_alembic_version_item(data: AlembicVersionCreate, db: AsyncSession = Depends()):
    db_item = DBAlembicVersion(**data.dict())
    return await create_alembic_version(db, db_item)