from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kalite_dosya import KaliteDosya

async def get_all_kalite_dosya(db: AsyncSession):
    result = await db.execute(select(KaliteDosya))
    return result.scalars().all()

async def get_kalite_dosya_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(KaliteDosya).where(KaliteDosya.id == id))
    return result.scalar_one_or_none()

async def create_kalite_dosya(db: AsyncSession, obj: KaliteDosya):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj