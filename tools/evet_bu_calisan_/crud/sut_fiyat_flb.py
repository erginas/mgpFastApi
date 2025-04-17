from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sut_fiyat_flb import SutFiyatFlb

async def get_all_sut_fiyat_flb(db: AsyncSession):
    result = await db.execute(select(SutFiyatFlb))
    return result.scalars().all()

async def get_sut_fiyat_flb_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SutFiyatFlb).where(SutFiyatFlb.id == id))
    return result.scalar_one_or_none()

async def create_sut_fiyat_flb(db: AsyncSession, obj: SutFiyatFlb):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj