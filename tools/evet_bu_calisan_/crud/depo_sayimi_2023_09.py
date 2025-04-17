from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2023_09 import DepoSayimi202309

async def get_all_depo_sayimi_2023_09(db: AsyncSession):
    result = await db.execute(select(DepoSayimi202309))
    return result.scalars().all()

async def get_depo_sayimi_2023_09_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi202309).where(DepoSayimi202309.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2023_09(db: AsyncSession, obj: DepoSayimi202309):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj