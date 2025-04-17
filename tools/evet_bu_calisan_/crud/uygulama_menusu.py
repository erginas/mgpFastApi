from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uygulama_menusu import UygulamaMenusu

async def get_all_uygulama_menusu(db: AsyncSession):
    result = await db.execute(select(UygulamaMenusu))
    return result.scalars().all()

async def get_uygulama_menusu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UygulamaMenusu).where(UygulamaMenusu.id == id))
    return result.scalar_one_or_none()

async def create_uygulama_menusu(db: AsyncSession, obj: UygulamaMenusu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj