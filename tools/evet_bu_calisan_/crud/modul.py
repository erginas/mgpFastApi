from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.modul import Modul

async def get_all_modul(db: AsyncSession):
    result = await db.execute(select(Modul))
    return result.scalars().all()

async def get_modul_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Modul).where(Modul.id == id))
    return result.scalar_one_or_none()

async def create_modul(db: AsyncSession, obj: Modul):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj