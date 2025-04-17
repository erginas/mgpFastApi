from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo import Depo

async def get_all_depo(db: AsyncSession):
    result = await db.execute(select(Depo))
    return result.scalars().all()

async def get_depo_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Depo).where(Depo.id == id))
    return result.scalar_one_or_none()

async def create_depo(db: AsyncSession, obj: Depo):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj