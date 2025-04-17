from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_yetkilisi import DepoYetkilisi

async def get_all_depo_yetkilisi(db: AsyncSession):
    result = await db.execute(select(DepoYetkilisi))
    return result.scalars().all()

async def get_depo_yetkilisi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoYetkilisi).where(DepoYetkilisi.id == id))
    return result.scalar_one_or_none()

async def create_depo_yetkilisi(db: AsyncSession, obj: DepoYetkilisi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj