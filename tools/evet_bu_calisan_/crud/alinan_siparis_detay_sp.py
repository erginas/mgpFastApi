from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.alinan_siparis_detay_sp import AlinanSiparisDetaySp

async def get_all_alinan_siparis_detay_sp(db: AsyncSession):
    result = await db.execute(select(AlinanSiparisDetaySp))
    return result.scalars().all()

async def get_alinan_siparis_detay_sp_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AlinanSiparisDetaySp).where(AlinanSiparisDetaySp.id == id))
    return result.scalar_one_or_none()

async def create_alinan_siparis_detay_sp(db: AsyncSession, obj: AlinanSiparisDetaySp):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj