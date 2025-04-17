from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.gecici_stok import GeciciStok

async def get_all_gecici_stok(db: AsyncSession):
    result = await db.execute(select(GeciciStok))
    return result.scalars().all()

async def get_gecici_stok_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(GeciciStok).where(GeciciStok.id == id))
    return result.scalar_one_or_none()

async def create_gecici_stok(db: AsyncSession, obj: GeciciStok):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj