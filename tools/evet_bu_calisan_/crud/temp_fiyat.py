from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.temp_fiyat import TempFiyat

async def get_all_temp_fiyat(db: AsyncSession):
    result = await db.execute(select(TempFiyat))
    return result.scalars().all()

async def get_temp_fiyat_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TempFiyat).where(TempFiyat.id == id))
    return result.scalar_one_or_none()

async def create_temp_fiyat(db: AsyncSession, obj: TempFiyat):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj