from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.toplanti import Toplanti

async def get_all_toplanti(db: AsyncSession):
    result = await db.execute(select(Toplanti))
    return result.scalars().all()

async def get_toplanti_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Toplanti).where(Toplanti.id == id))
    return result.scalar_one_or_none()

async def create_toplanti(db: AsyncSession, obj: Toplanti):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj