from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uygunsuzluk_sorumlusu import UygunsuzlukSorumlusu

async def get_all_uygunsuzluk_sorumlusu(db: AsyncSession):
    result = await db.execute(select(UygunsuzlukSorumlusu))
    return result.scalars().all()

async def get_uygunsuzluk_sorumlusu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UygunsuzlukSorumlusu).where(UygunsuzlukSorumlusu.id == id))
    return result.scalar_one_or_none()

async def create_uygunsuzluk_sorumlusu(db: AsyncSession, obj: UygunsuzlukSorumlusu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj