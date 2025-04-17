from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.performans_verisi import PerformansVerisi

async def get_all_performans_verisi(db: AsyncSession):
    result = await db.execute(select(PerformansVerisi))
    return result.scalars().all()

async def get_performans_verisi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(PerformansVerisi).where(PerformansVerisi.id == id))
    return result.scalar_one_or_none()

async def create_performans_verisi(db: AsyncSession, obj: PerformansVerisi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj