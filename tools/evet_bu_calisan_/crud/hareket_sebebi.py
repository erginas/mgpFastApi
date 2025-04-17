from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.hareket_sebebi import HareketSebebi

async def get_all_hareket_sebebi(db: AsyncSession):
    result = await db.execute(select(HareketSebebi))
    return result.scalars().all()

async def get_hareket_sebebi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(HareketSebebi).where(HareketSebebi.id == id))
    return result.scalar_one_or_none()

async def create_hareket_sebebi(db: AsyncSession, obj: HareketSebebi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj