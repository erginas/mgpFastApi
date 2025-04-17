from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.urun_alternatifi import UrunAlternatifi

async def get_all_urun_alternatifi(db: AsyncSession):
    result = await db.execute(select(UrunAlternatifi))
    return result.scalars().all()

async def get_urun_alternatifi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UrunAlternatifi).where(UrunAlternatifi.id == id))
    return result.scalar_one_or_none()

async def create_urun_alternatifi(db: AsyncSession, obj: UrunAlternatifi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj