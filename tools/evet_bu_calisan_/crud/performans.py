from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.performans import Performans

async def get_all_performans(db: AsyncSession):
    result = await db.execute(select(Performans))
    return result.scalars().all()

async def get_performans_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Performans).where(Performans.id == id))
    return result.scalar_one_or_none()

async def create_performans(db: AsyncSession, obj: Performans):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj