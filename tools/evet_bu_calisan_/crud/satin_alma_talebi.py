from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.satin_alma_talebi import SatinAlmaTalebi

async def get_all_satin_alma_talebi(db: AsyncSession):
    result = await db.execute(select(SatinAlmaTalebi))
    return result.scalars().all()

async def get_satin_alma_talebi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SatinAlmaTalebi).where(SatinAlmaTalebi.id == id))
    return result.scalar_one_or_none()

async def create_satin_alma_talebi(db: AsyncSession, obj: SatinAlmaTalebi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj