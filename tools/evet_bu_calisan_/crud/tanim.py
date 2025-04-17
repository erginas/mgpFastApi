from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tanim import Tanim

async def get_all_tanim(db: AsyncSession):
    result = await db.execute(select(Tanim))
    return result.scalars().all()

async def get_tanim_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Tanim).where(Tanim.id == id))
    return result.scalar_one_or_none()

async def create_tanim(db: AsyncSession, obj: Tanim):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj