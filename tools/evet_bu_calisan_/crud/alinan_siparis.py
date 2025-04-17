from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.alinan_siparis import AlinanSiparis

async def get_all_alinan_siparis(db: AsyncSession):
    result = await db.execute(select(AlinanSiparis))
    return result.scalars().all()

async def get_alinan_siparis_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AlinanSiparis).where(AlinanSiparis.id == id))
    return result.scalar_one_or_none()

async def create_alinan_siparis(db: AsyncSession, obj: AlinanSiparis):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj