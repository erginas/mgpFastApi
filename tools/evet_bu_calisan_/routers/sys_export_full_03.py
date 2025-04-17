from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sys_export_full_03 import SysExportFull03, SysExportFull03Create
from models.sys_export_full_03 import SysExportFull03 as DBSysExportFull03
from crud.sys_export_full_03 import get_all_sys_export_full_03, get_sys_export_full_03_by_id, create_sys_export_full_03

router = APIRouter(prefix='/sys_export_full_03', tags=['SysExportFull03'])

@router.get('/', response_model=list[SysExportFull03])
async def list_sys_export_full_03(db: AsyncSession = Depends()):
    return await get_all_sys_export_full_03(db)

@router.get('/{id}', response_model=SysExportFull03)
async def get_sys_export_full_03_item(id: int, db: AsyncSession = Depends()):
    result = await get_sys_export_full_03_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SysExportFull03)
async def create_sys_export_full_03_item(data: SysExportFull03Create, db: AsyncSession = Depends()):
    db_item = DBSysExportFull03(**data.dict())
    return await create_sys_export_full_03(db, db_item)