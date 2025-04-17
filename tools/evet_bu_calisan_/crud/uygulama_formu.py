from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uygulama_formu import UygulamaFormu

async def get_all_uygulama_formu(db: AsyncSession):
    result = await db.execute(select(UygulamaFormu))
    return result.scalars().all()

async def get_uygulama_formu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UygulamaFormu).where(UygulamaFormu.id == id))
    return result.scalar_one_or_none()

async def create_uygulama_formu(db: AsyncSession, obj: UygulamaFormu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj