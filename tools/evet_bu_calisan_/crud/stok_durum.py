from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.stok_durum import StokDurum

async def get_all_stok_durum(db: AsyncSession):
    result = await db.execute(select(StokDurum))
    return result.scalars().all()

async def get_stok_durum_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(StokDurum).where(StokDurum.id == id))
    return result.scalar_one_or_none()

async def create_stok_durum(db: AsyncSession, obj: StokDurum):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj