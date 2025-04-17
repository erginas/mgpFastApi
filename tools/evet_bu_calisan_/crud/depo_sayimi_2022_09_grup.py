from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2022_09_grup import DepoSayimi202209Grup

async def get_all_depo_sayimi_2022_09_grup(db: AsyncSession):
    result = await db.execute(select(DepoSayimi202209Grup))
    return result.scalars().all()

async def get_depo_sayimi_2022_09_grup_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi202209Grup).where(DepoSayimi202209Grup.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2022_09_grup(db: AsyncSession, obj: DepoSayimi202209Grup):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj