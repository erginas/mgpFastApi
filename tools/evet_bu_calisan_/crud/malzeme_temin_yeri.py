from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_temin_yeri import MalzemeTeminYeri

async def get_all_malzeme_temin_yeri(db: AsyncSession):
    result = await db.execute(select(MalzemeTeminYeri))
    return result.scalars().all()

async def get_malzeme_temin_yeri_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeTeminYeri).where(MalzemeTeminYeri.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_temin_yeri(db: AsyncSession, obj: MalzemeTeminYeri):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj