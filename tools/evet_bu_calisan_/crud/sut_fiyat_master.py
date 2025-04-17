from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sut_fiyat_master import SutFiyatMaster

async def get_all_sut_fiyat_master(db: AsyncSession):
    result = await db.execute(select(SutFiyatMaster))
    return result.scalars().all()

async def get_sut_fiyat_master_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SutFiyatMaster).where(SutFiyatMaster.id == id))
    return result.scalar_one_or_none()

async def create_sut_fiyat_master(db: AsyncSession, obj: SutFiyatMaster):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj