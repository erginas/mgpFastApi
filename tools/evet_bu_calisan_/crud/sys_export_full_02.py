from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sys_export_full_02 import SysExportFull02

async def get_all_sys_export_full_02(db: AsyncSession):
    result = await db.execute(select(SysExportFull02))
    return result.scalars().all()

async def get_sys_export_full_02_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SysExportFull02).where(SysExportFull02.id == id))
    return result.scalar_one_or_none()

async def create_sys_export_full_02(db: AsyncSession, obj: SysExportFull02):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj