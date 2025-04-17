from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_hareket_sebebi import DepoHareketSebebi

async def get_all_depo_hareket_sebebi(db: AsyncSession):
    result = await db.execute(select(DepoHareketSebebi))
    return result.scalars().all()

async def get_depo_hareket_sebebi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoHareketSebebi).where(DepoHareketSebebi.id == id))
    return result.scalar_one_or_none()

async def create_depo_hareket_sebebi(db: AsyncSession, obj: DepoHareketSebebi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj