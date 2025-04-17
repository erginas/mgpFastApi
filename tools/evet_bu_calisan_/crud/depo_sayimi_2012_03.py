from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2012_03 import DepoSayimi201203

async def get_all_depo_sayimi_2012_03(db: AsyncSession):
    result = await db.execute(select(DepoSayimi201203))
    return result.scalars().all()

async def get_depo_sayimi_2012_03_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi201203).where(DepoSayimi201203.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2012_03(db: AsyncSession, obj: DepoSayimi201203):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj