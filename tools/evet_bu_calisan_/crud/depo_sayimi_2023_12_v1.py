from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2023_12_v1 import DepoSayimi202312V1

async def get_all_depo_sayimi_2023_12_v1(db: AsyncSession):
    result = await db.execute(select(DepoSayimi202312V1))
    return result.scalars().all()

async def get_depo_sayimi_2023_12_v1_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi202312V1).where(DepoSayimi202312V1.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2023_12_v1(db: AsyncSession, obj: DepoSayimi202312V1):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj