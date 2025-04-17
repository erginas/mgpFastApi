from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sys_export_full_01 import SysExportFull01, SysExportFull01Create
from models.sys_export_full_01 import SysExportFull01 as DBSysExportFull01
from crud.sys_export_full_01 import get_all_sys_export_full_01, get_sys_export_full_01_by_id, create_sys_export_full_01

router = APIRouter(prefix='/sys_export_full_01', tags=['SysExportFull01'])

@router.get('/', response_model=list[SysExportFull01])
async def list_sys_export_full_01(db: AsyncSession = Depends()):
    return await get_all_sys_export_full_01(db)

@router.get('/{id}', response_model=SysExportFull01)
async def get_sys_export_full_01_item(id: int, db: AsyncSession = Depends()):
    result = await get_sys_export_full_01_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SysExportFull01)
async def create_sys_export_full_01_item(data: SysExportFull01Create, db: AsyncSession = Depends()):
    db_item = DBSysExportFull01(**data.dict())
    return await create_sys_export_full_01(db, db_item)