from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.ozellik_sinifi import OzellikSinifi

async def get_all_ozellik_sinifi(db: AsyncSession):
    result = await db.execute(select(OzellikSinifi))
    return result.scalars().all()

async def get_ozellik_sinifi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(OzellikSinifi).where(OzellikSinifi.id == id))
    return result.scalar_one_or_none()

async def create_ozellik_sinifi(db: AsyncSession, obj: OzellikSinifi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj