from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.resim import Resim

async def get_all_resim(db: AsyncSession):
    result = await db.execute(select(Resim))
    return result.scalars().all()

async def get_resim_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Resim).where(Resim.id == id))
    return result.scalar_one_or_none()

async def create_resim(db: AsyncSession, obj: Resim):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj