from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uygunsuzluk_gorus_bildiren import UygunsuzlukGorusBildiren

async def get_all_uygunsuzluk_gorus_bildiren(db: AsyncSession):
    result = await db.execute(select(UygunsuzlukGorusBildiren))
    return result.scalars().all()

async def get_uygunsuzluk_gorus_bildiren_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UygunsuzlukGorusBildiren).where(UygunsuzlukGorusBildiren.id == id))
    return result.scalar_one_or_none()

async def create_uygunsuzluk_gorus_bildiren(db: AsyncSession, obj: UygunsuzlukGorusBildiren):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj