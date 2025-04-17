from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2013_02 import DepoSayimi201302

async def get_all_depo_sayimi_2013_02(db: AsyncSession):
    result = await db.execute(select(DepoSayimi201302))
    return result.scalars().all()

async def get_depo_sayimi_2013_02_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi201302).where(DepoSayimi201302.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2013_02(db: AsyncSession, obj: DepoSayimi201302):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj