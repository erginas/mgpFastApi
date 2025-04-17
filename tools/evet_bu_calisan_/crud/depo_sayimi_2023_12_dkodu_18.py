from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2023_12_dkodu_18 import DepoSayimi202312Dkodu18

async def get_all_depo_sayimi_2023_12_dkodu_18(db: AsyncSession):
    result = await db.execute(select(DepoSayimi202312Dkodu18))
    return result.scalars().all()

async def get_depo_sayimi_2023_12_dkodu_18_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi202312Dkodu18).where(DepoSayimi202312Dkodu18.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2023_12_dkodu_18(db: AsyncSession, obj: DepoSayimi202312Dkodu18):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj