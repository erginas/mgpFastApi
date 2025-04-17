from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.giris_kalite_detay import GirisKaliteDetay

async def get_all_giris_kalite_detay(db: AsyncSession):
    result = await db.execute(select(GirisKaliteDetay))
    return result.scalars().all()

async def get_giris_kalite_detay_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(GirisKaliteDetay).where(GirisKaliteDetay.id == id))
    return result.scalar_one_or_none()

async def create_giris_kalite_detay(db: AsyncSession, obj: GirisKaliteDetay):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj