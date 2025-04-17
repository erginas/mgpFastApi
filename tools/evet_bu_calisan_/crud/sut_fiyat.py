from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sut_fiyat import SutFiyat

async def get_all_sut_fiyat(db: AsyncSession):
    result = await db.execute(select(SutFiyat))
    return result.scalars().all()

async def get_sut_fiyat_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SutFiyat).where(SutFiyat.id == id))
    return result.scalar_one_or_none()

async def create_sut_fiyat(db: AsyncSession, obj: SutFiyat):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj