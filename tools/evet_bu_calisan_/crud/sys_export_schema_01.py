from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sys_export_schema_01 import SysExportSchema01

async def get_all_sys_export_schema_01(db: AsyncSession):
    result = await db.execute(select(SysExportSchema01))
    return result.scalars().all()

async def get_sys_export_schema_01_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SysExportSchema01).where(SysExportSchema01.id == id))
    return result.scalar_one_or_none()

async def create_sys_export_schema_01(db: AsyncSession, obj: SysExportSchema01):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj