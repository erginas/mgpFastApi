from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sys_export_full_03 import SysExportFull03

async def get_all_sys_export_full_03(db: AsyncSession):
    result = await db.execute(select(SysExportFull03))
    return result.scalars().all()

async def get_sys_export_full_03_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SysExportFull03).where(SysExportFull03.id == id))
    return result.scalar_one_or_none()

async def create_sys_export_full_03(db: AsyncSession, obj: SysExportFull03):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj