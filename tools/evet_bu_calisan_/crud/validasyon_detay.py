from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.validasyon_detay import ValidasyonDetay

async def get_all_validasyon_detay(db: AsyncSession):
    result = await db.execute(select(ValidasyonDetay))
    return result.scalars().all()

async def get_validasyon_detay_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ValidasyonDetay).where(ValidasyonDetay.id == id))
    return result.scalar_one_or_none()

async def create_validasyon_detay(db: AsyncSession, obj: ValidasyonDetay):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj