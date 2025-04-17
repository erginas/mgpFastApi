from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2023_12_5_106 import DepoSayimi2023125106

async def get_all_depo_sayimi_2023_12_5_106(db: AsyncSession):
    result = await db.execute(select(DepoSayimi2023125106))
    return result.scalars().all()

async def get_depo_sayimi_2023_12_5_106_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi2023125106).where(DepoSayimi2023125106.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2023_12_5_106(db: AsyncSession, obj: DepoSayimi2023125106):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj