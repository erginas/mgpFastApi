from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.alinan_siparis_sevkiyati import AlinanSiparisSevkiyati

async def get_all_alinan_siparis_sevkiyati(db: AsyncSession):
    result = await db.execute(select(AlinanSiparisSevkiyati))
    return result.scalars().all()

async def get_alinan_siparis_sevkiyati_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AlinanSiparisSevkiyati).where(AlinanSiparisSevkiyati.id == id))
    return result.scalar_one_or_none()

async def create_alinan_siparis_sevkiyati(db: AsyncSession, obj: AlinanSiparisSevkiyati):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj