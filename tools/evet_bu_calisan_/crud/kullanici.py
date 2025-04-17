from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kullanici import Kullanici

async def get_all_kullanici(db: AsyncSession):
    result = await db.execute(select(Kullanici))
    return result.scalars().all()

async def get_kullanici_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Kullanici).where(Kullanici.id == id))
    return result.scalar_one_or_none()

async def create_kullanici(db: AsyncSession, obj: Kullanici):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj