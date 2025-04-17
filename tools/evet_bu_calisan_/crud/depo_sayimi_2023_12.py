from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2023_12 import DepoSayimi202312

async def get_all_depo_sayimi_2023_12(db: AsyncSession):
    result = await db.execute(select(DepoSayimi202312))
    return result.scalars().all()

async def get_depo_sayimi_2023_12_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi202312).where(DepoSayimi202312.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2023_12(db: AsyncSession, obj: DepoSayimi202312):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj