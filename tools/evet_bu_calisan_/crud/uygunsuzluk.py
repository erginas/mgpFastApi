from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uygunsuzluk import Uygunsuzluk

async def get_all_uygunsuzluk(db: AsyncSession):
    result = await db.execute(select(Uygunsuzluk))
    return result.scalars().all()

async def get_uygunsuzluk_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Uygunsuzluk).where(Uygunsuzluk.id == id))
    return result.scalar_one_or_none()

async def create_uygunsuzluk(db: AsyncSession, obj: Uygunsuzluk):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj