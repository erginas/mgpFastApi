from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.gerekcelendirme import Gerekcelendirme

async def get_all_gerekcelendirme(db: AsyncSession):
    result = await db.execute(select(Gerekcelendirme))
    return result.scalars().all()

async def get_gerekcelendirme_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Gerekcelendirme).where(Gerekcelendirme.id == id))
    return result.scalar_one_or_none()

async def create_gerekcelendirme(db: AsyncSession, obj: Gerekcelendirme):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj