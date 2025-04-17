from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_temin_sekli import MalzemeTeminSekli

async def get_all_malzeme_temin_sekli(db: AsyncSession):
    result = await db.execute(select(MalzemeTeminSekli))
    return result.scalars().all()

async def get_malzeme_temin_sekli_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeTeminSekli).where(MalzemeTeminSekli.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_temin_sekli(db: AsyncSession, obj: MalzemeTeminSekli):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj