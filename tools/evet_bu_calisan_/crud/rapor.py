from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.rapor import Rapor

async def get_all_rapor(db: AsyncSession):
    result = await db.execute(select(Rapor))
    return result.scalars().all()

async def get_rapor_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Rapor).where(Rapor.id == id))
    return result.scalar_one_or_none()

async def create_rapor(db: AsyncSession, obj: Rapor):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj