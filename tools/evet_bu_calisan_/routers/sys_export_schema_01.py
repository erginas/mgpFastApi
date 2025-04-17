from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sys_export_schema_01 import SysExportSchema01, SysExportSchema01Create
from models.sys_export_schema_01 import SysExportSchema01 as DBSysExportSchema01
from crud.sys_export_schema_01 import get_all_sys_export_schema_01, get_sys_export_schema_01_by_id, create_sys_export_schema_01

router = APIRouter(prefix='/sys_export_schema_01', tags=['SysExportSchema01'])

@router.get('/', response_model=list[SysExportSchema01])
async def list_sys_export_schema_01(db: AsyncSession = Depends()):
    return await get_all_sys_export_schema_01(db)

@router.get('/{id}', response_model=SysExportSchema01)
async def get_sys_export_schema_01_item(id: int, db: AsyncSession = Depends()):
    result = await get_sys_export_schema_01_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SysExportSchema01)
async def create_sys_export_schema_01_item(data: SysExportSchema01Create, db: AsyncSession = Depends()):
    db_item = DBSysExportSchema01(**data.dict())
    return await create_sys_export_schema_01(db, db_item)