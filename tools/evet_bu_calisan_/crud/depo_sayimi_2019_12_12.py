from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2019_12_12 import DepoSayimi20191212

async def get_all_depo_sayimi_2019_12_12(db: AsyncSession):
    result = await db.execute(select(DepoSayimi20191212))
    return result.scalars().all()

async def get_depo_sayimi_2019_12_12_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi20191212).where(DepoSayimi20191212.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2019_12_12(db: AsyncSession, obj: DepoSayimi20191212):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj