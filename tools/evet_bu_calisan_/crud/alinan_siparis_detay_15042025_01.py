from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.alinan_siparis_detay_15042025_01 import AlinanSiparisDetay1504202501

async def get_all_alinan_siparis_detay_15042025_01(db: AsyncSession):
    result = await db.execute(select(AlinanSiparisDetay1504202501))
    return result.scalars().all()

async def get_alinan_siparis_detay_15042025_01_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AlinanSiparisDetay1504202501).where(AlinanSiparisDetay1504202501.id == id))
    return result.scalar_one_or_none()

async def create_alinan_siparis_detay_15042025_01(db: AsyncSession, obj: AlinanSiparisDetay1504202501):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj