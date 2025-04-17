from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kisi import Kisi

async def get_all_kisi(db: AsyncSession):
    result = await db.execute(select(Kisi))
    return result.scalars().all()

async def get_kisi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Kisi).where(Kisi.id == id))
    return result.scalar_one_or_none()

async def create_kisi(db: AsyncSession, obj: Kisi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj