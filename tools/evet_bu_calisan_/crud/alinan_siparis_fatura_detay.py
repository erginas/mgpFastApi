from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.alinan_siparis_fatura_detay import AlinanSiparisFaturaDetay

async def get_all_alinan_siparis_fatura_detay(db: AsyncSession):
    result = await db.execute(select(AlinanSiparisFaturaDetay))
    return result.scalars().all()

async def get_alinan_siparis_fatura_detay_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AlinanSiparisFaturaDetay).where(AlinanSiparisFaturaDetay.id == id))
    return result.scalar_one_or_none()

async def create_alinan_siparis_fatura_detay(db: AsyncSession, obj: AlinanSiparisFaturaDetay):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj