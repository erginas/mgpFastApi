from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uts_baslik import UtsBaslik

async def get_all_uts_baslik(db: AsyncSession):
    result = await db.execute(select(UtsBaslik))
    return result.scalars().all()

async def get_uts_baslik_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UtsBaslik).where(UtsBaslik.id == id))
    return result.scalar_one_or_none()

async def create_uts_baslik(db: AsyncSession, obj: UtsBaslik):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj