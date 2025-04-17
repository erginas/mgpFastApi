from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.alinan_siparis_detay_15042025 import AlinanSiparisDetay15042025

async def get_all_alinan_siparis_detay_15042025(db: AsyncSession):
    result = await db.execute(select(AlinanSiparisDetay15042025))
    return result.scalars().all()

async def get_alinan_siparis_detay_15042025_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AlinanSiparisDetay15042025).where(AlinanSiparisDetay15042025.id == id))
    return result.scalar_one_or_none()

async def create_alinan_siparis_detay_15042025(db: AsyncSession, obj: AlinanSiparisDetay15042025):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj