from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2006_01 import DepoSayimi200601

async def get_all_depo_sayimi_2006_01(db: AsyncSession):
    result = await db.execute(select(DepoSayimi200601))
    return result.scalars().all()

async def get_depo_sayimi_2006_01_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi200601).where(DepoSayimi200601.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2006_01(db: AsyncSession, obj: DepoSayimi200601):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj