from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sys_export_full_04 import SysExportFull04

async def get_all_sys_export_full_04(db: AsyncSession):
    result = await db.execute(select(SysExportFull04))
    return result.scalars().all()

async def get_sys_export_full_04_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SysExportFull04).where(SysExportFull04.id == id))
    return result.scalar_one_or_none()

async def create_sys_export_full_04(db: AsyncSession, obj: SysExportFull04):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj