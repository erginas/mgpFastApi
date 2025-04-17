from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.ulke import Ulke

async def get_all_ulke(db: AsyncSession):
    result = await db.execute(select(Ulke))
    return result.scalars().all()

async def get_ulke_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Ulke).where(Ulke.id == id))
    return result.scalar_one_or_none()

async def create_ulke(db: AsyncSession, obj: Ulke):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj