from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.gorus import Gorus

async def get_all_gorus(db: AsyncSession):
    result = await db.execute(select(Gorus))
    return result.scalars().all()

async def get_gorus_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Gorus).where(Gorus.id == id))
    return result.scalar_one_or_none()

async def create_gorus(db: AsyncSession, obj: Gorus):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj