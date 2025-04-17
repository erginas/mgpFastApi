from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sevkiyat_log import SevkiyatLog

async def get_all_sevkiyat_log(db: AsyncSession):
    result = await db.execute(select(SevkiyatLog))
    return result.scalars().all()

async def get_sevkiyat_log_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SevkiyatLog).where(SevkiyatLog.id == id))
    return result.scalar_one_or_none()

async def create_sevkiyat_log(db: AsyncSession, obj: SevkiyatLog):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj