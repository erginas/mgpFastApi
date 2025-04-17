from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sorgu_yetkilisi import SorguYetkilisi

async def get_all_sorgu_yetkilisi(db: AsyncSession):
    result = await db.execute(select(SorguYetkilisi))
    return result.scalars().all()

async def get_sorgu_yetkilisi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SorguYetkilisi).where(SorguYetkilisi.id == id))
    return result.scalar_one_or_none()

async def create_sorgu_yetkilisi(db: AsyncSession, obj: SorguYetkilisi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj