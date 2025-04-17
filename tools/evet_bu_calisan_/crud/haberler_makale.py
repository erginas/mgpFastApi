from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.haberler_makale import HaberlerMakale

async def get_all_haberler_makale(db: AsyncSession):
    result = await db.execute(select(HaberlerMakale))
    return result.scalars().all()

async def get_haberler_makale_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(HaberlerMakale).where(HaberlerMakale.id == id))
    return result.scalar_one_or_none()

async def create_haberler_makale(db: AsyncSession, obj: HaberlerMakale):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj