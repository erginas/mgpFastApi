from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.gecici_stok_detay import GeciciStokDetay

async def get_all_gecici_stok_detay(db: AsyncSession):
    result = await db.execute(select(GeciciStokDetay))
    return result.scalars().all()

async def get_gecici_stok_detay_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(GeciciStokDetay).where(GeciciStokDetay.id == id))
    return result.scalar_one_or_none()

async def create_gecici_stok_detay(db: AsyncSession, obj: GeciciStokDetay):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj