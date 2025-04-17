from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2019_12 import DepoSayimi201912

async def get_all_depo_sayimi_2019_12(db: AsyncSession):
    result = await db.execute(select(DepoSayimi201912))
    return result.scalars().all()

async def get_depo_sayimi_2019_12_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi201912).where(DepoSayimi201912.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2019_12(db: AsyncSession, obj: DepoSayimi201912):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj