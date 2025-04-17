from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sys_export_full_04 import SysExportFull04, SysExportFull04Create
from models.sys_export_full_04 import SysExportFull04 as DBSysExportFull04
from crud.sys_export_full_04 import get_all_sys_export_full_04, get_sys_export_full_04_by_id, create_sys_export_full_04

router = APIRouter(prefix='/sys_export_full_04', tags=['SysExportFull04'])

@router.get('/', response_model=list[SysExportFull04])
async def list_sys_export_full_04(db: AsyncSession = Depends()):
    return await get_all_sys_export_full_04(db)

@router.get('/{id}', response_model=SysExportFull04)
async def get_sys_export_full_04_item(id: int, db: AsyncSession = Depends()):
    result = await get_sys_export_full_04_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SysExportFull04)
async def create_sys_export_full_04_item(data: SysExportFull04Create, db: AsyncSession = Depends()):
    db_item = DBSysExportFull04(**data.dict())
    return await create_sys_export_full_04(db, db_item)