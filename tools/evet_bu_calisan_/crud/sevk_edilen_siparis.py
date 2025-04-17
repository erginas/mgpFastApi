from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sevk_edilen_siparis import SevkEdilenSiparis

async def get_all_sevk_edilen_siparis(db: AsyncSession):
    result = await db.execute(select(SevkEdilenSiparis))
    return result.scalars().all()

async def get_sevk_edilen_siparis_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SevkEdilenSiparis).where(SevkEdilenSiparis.id == id))
    return result.scalar_one_or_none()

async def create_sevk_edilen_siparis(db: AsyncSession, obj: SevkEdilenSiparis):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj