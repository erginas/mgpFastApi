from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.atama import Atama

async def get_all_atama(db: AsyncSession):
    result = await db.execute(select(Atama))
    return result.scalars().all()

async def get_atama_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Atama).where(Atama.id == id))
    return result.scalar_one_or_none()

async def create_atama(db: AsyncSession, obj: Atama):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj