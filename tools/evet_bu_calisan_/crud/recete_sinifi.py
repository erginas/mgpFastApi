from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.recete_sinifi import ReceteSinifi

async def get_all_recete_sinifi(db: AsyncSession):
    result = await db.execute(select(ReceteSinifi))
    return result.scalars().all()

async def get_recete_sinifi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ReceteSinifi).where(ReceteSinifi.id == id))
    return result.scalar_one_or_none()

async def create_recete_sinifi(db: AsyncSession, obj: ReceteSinifi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj