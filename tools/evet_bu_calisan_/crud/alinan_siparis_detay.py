from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.alinan_siparis_detay import AlinanSiparisDetay

async def get_all_alinan_siparis_detay(db: AsyncSession):
    result = await db.execute(select(AlinanSiparisDetay))
    return result.scalars().all()

async def get_alinan_siparis_detay_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AlinanSiparisDetay).where(AlinanSiparisDetay.id == id))
    return result.scalar_one_or_none()

async def create_alinan_siparis_detay(db: AsyncSession, obj: AlinanSiparisDetay):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj