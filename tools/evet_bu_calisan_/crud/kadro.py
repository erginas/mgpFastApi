from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kadro import Kadro

async def get_all_kadro(db: AsyncSession):
    result = await db.execute(select(Kadro))
    return result.scalars().all()

async def get_kadro_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Kadro).where(Kadro.id == id))
    return result.scalar_one_or_none()

async def create_kadro(db: AsyncSession, obj: Kadro):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj