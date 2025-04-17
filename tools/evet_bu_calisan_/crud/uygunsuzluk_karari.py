from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uygunsuzluk_karari import UygunsuzlukKarari

async def get_all_uygunsuzluk_karari(db: AsyncSession):
    result = await db.execute(select(UygunsuzlukKarari))
    return result.scalars().all()

async def get_uygunsuzluk_karari_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UygunsuzlukKarari).where(UygunsuzlukKarari.id == id))
    return result.scalar_one_or_none()

async def create_uygunsuzluk_karari(db: AsyncSession, obj: UygunsuzlukKarari):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj