from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2025_01 import DepoSayimi202501

async def get_all_depo_sayimi_2025_01(db: AsyncSession):
    result = await db.execute(select(DepoSayimi202501))
    return result.scalars().all()

async def get_depo_sayimi_2025_01_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi202501).where(DepoSayimi202501.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2025_01(db: AsyncSession, obj: DepoSayimi202501):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj