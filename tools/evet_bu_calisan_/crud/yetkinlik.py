from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.yetkinlik import Yetkinlik

async def get_all_yetkinlik(db: AsyncSession):
    result = await db.execute(select(Yetkinlik))
    return result.scalars().all()

async def get_yetkinlik_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Yetkinlik).where(Yetkinlik.id == id))
    return result.scalar_one_or_none()

async def create_yetkinlik(db: AsyncSession, obj: Yetkinlik):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj