from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uygunsuzluk_gorusu import UygunsuzlukGorusu

async def get_all_uygunsuzluk_gorusu(db: AsyncSession):
    result = await db.execute(select(UygunsuzlukGorusu))
    return result.scalars().all()

async def get_uygunsuzluk_gorusu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UygunsuzlukGorusu).where(UygunsuzlukGorusu.id == id))
    return result.scalar_one_or_none()

async def create_uygunsuzluk_gorusu(db: AsyncSession, obj: UygunsuzlukGorusu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj