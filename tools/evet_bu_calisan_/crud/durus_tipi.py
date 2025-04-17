from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.durus_tipi import DurusTipi

async def get_all_durus_tipi(db: AsyncSession):
    result = await db.execute(select(DurusTipi))
    return result.scalars().all()

async def get_durus_tipi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DurusTipi).where(DurusTipi.id == id))
    return result.scalar_one_or_none()

async def create_durus_tipi(db: AsyncSession, obj: DurusTipi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj