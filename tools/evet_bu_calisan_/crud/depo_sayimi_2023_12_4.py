from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2023_12_4 import DepoSayimi2023124

async def get_all_depo_sayimi_2023_12_4(db: AsyncSession):
    result = await db.execute(select(DepoSayimi2023124))
    return result.scalars().all()

async def get_depo_sayimi_2023_12_4_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi2023124).where(DepoSayimi2023124.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2023_12_4(db: AsyncSession, obj: DepoSayimi2023124):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj