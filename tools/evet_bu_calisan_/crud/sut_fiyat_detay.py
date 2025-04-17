from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sut_fiyat_detay import SutFiyatDetay

async def get_all_sut_fiyat_detay(db: AsyncSession):
    result = await db.execute(select(SutFiyatDetay))
    return result.scalars().all()

async def get_sut_fiyat_detay_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SutFiyatDetay).where(SutFiyatDetay.id == id))
    return result.scalar_one_or_none()

async def create_sut_fiyat_detay(db: AsyncSession, obj: SutFiyatDetay):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj