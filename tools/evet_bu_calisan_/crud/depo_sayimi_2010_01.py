from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2010_01 import DepoSayimi201001

async def get_all_depo_sayimi_2010_01(db: AsyncSession):
    result = await db.execute(select(DepoSayimi201001))
    return result.scalars().all()

async def get_depo_sayimi_2010_01_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi201001).where(DepoSayimi201001.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2010_01(db: AsyncSession, obj: DepoSayimi201001):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj