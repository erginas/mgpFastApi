from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.gecici_stok_favori import GeciciStokFavori

async def get_all_gecici_stok_favori(db: AsyncSession):
    result = await db.execute(select(GeciciStokFavori))
    return result.scalars().all()

async def get_gecici_stok_favori_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(GeciciStokFavori).where(GeciciStokFavori.id == id))
    return result.scalar_one_or_none()

async def create_gecici_stok_favori(db: AsyncSession, obj: GeciciStokFavori):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj