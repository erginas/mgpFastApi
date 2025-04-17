from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uygunsuzluk_resim import UygunsuzlukResim

async def get_all_uygunsuzluk_resim(db: AsyncSession):
    result = await db.execute(select(UygunsuzlukResim))
    return result.scalars().all()

async def get_uygunsuzluk_resim_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UygunsuzlukResim).where(UygunsuzlukResim.id == id))
    return result.scalar_one_or_none()

async def create_uygunsuzluk_resim(db: AsyncSession, obj: UygunsuzlukResim):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj