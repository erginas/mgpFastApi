from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.alinan_siparis_fatura import AlinanSiparisFatura

async def get_all_alinan_siparis_fatura(db: AsyncSession):
    result = await db.execute(select(AlinanSiparisFatura))
    return result.scalars().all()

async def get_alinan_siparis_fatura_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AlinanSiparisFatura).where(AlinanSiparisFatura.id == id))
    return result.scalar_one_or_none()

async def create_alinan_siparis_fatura(db: AsyncSession, obj: AlinanSiparisFatura):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj