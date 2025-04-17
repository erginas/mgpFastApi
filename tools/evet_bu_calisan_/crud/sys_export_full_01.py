from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sys_export_full_01 import SysExportFull01

async def get_all_sys_export_full_01(db: AsyncSession):
    result = await db.execute(select(SysExportFull01))
    return result.scalars().all()

async def get_sys_export_full_01_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SysExportFull01).where(SysExportFull01.id == id))
    return result.scalar_one_or_none()

async def create_sys_export_full_01(db: AsyncSession, obj: SysExportFull01):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj