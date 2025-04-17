from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uygunsuzluk_detay import UygunsuzlukDetay

async def get_all_uygunsuzluk_detay(db: AsyncSession):
    result = await db.execute(select(UygunsuzlukDetay))
    return result.scalars().all()

async def get_uygunsuzluk_detay_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UygunsuzlukDetay).where(UygunsuzlukDetay.id == id))
    return result.scalar_one_or_none()

async def create_uygunsuzluk_detay(db: AsyncSession, obj: UygunsuzlukDetay):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj