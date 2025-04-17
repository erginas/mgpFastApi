from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.django_migrations import DjangoMigrations, DjangoMigrationsCreate
from models.django_migrations import DjangoMigrations as DBDjangoMigrations
from crud.django_migrations import get_all_django_migrations, get_django_migrations_by_id, create_django_migrations

router = APIRouter(prefix='/django_migrations', tags=['DjangoMigrations'])

@router.get('/', response_model=list[DjangoMigrations])
async def list_django_migrations(db: AsyncSession = Depends()):
    return await get_all_django_migrations(db)

@router.get('/{id}', response_model=DjangoMigrations)
async def get_django_migrations_item(id: int, db: AsyncSession = Depends()):
    result = await get_django_migrations_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DjangoMigrations)
async def create_django_migrations_item(data: DjangoMigrationsCreate, db: AsyncSession = Depends()):
    db_item = DBDjangoMigrations(**data.dict())
    return await create_django_migrations(db, db_item)