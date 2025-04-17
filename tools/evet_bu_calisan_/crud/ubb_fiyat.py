from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.ubb_fiyat import UbbFiyat

async def get_all_ubb_fiyat(db: AsyncSession):
    result = await db.execute(select(UbbFiyat))
    return result.scalars().all()

async def get_ubb_fiyat_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UbbFiyat).where(UbbFiyat.id == id))
    return result.scalar_one_or_none()

async def create_ubb_fiyat(db: AsyncSession, obj: UbbFiyat):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj