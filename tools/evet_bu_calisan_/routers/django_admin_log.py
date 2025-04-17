from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.django_admin_log import DjangoAdminLog, DjangoAdminLogCreate
from models.django_admin_log import DjangoAdminLog as DBDjangoAdminLog
from crud.django_admin_log import get_all_django_admin_log, get_django_admin_log_by_id, create_django_admin_log

router = APIRouter(prefix='/django_admin_log', tags=['DjangoAdminLog'])

@router.get('/', response_model=list[DjangoAdminLog])
async def list_django_admin_log(db: AsyncSession = Depends()):
    return await get_all_django_admin_log(db)

@router.get('/{id}', response_model=DjangoAdminLog)
async def get_django_admin_log_item(id: int, db: AsyncSession = Depends()):
    result = await get_django_admin_log_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DjangoAdminLog)
async def create_django_admin_log_item(data: DjangoAdminLogCreate, db: AsyncSession = Depends()):
    db_item = DBDjangoAdminLog(**data.dict())
    return await create_django_admin_log(db, db_item)