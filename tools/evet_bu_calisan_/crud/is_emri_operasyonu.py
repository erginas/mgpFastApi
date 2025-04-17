from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.is_emri_operasyonu import IsEmriOperasyonu

async def get_all_is_emri_operasyonu(db: AsyncSession):
    result = await db.execute(select(IsEmriOperasyonu))
    return result.scalars().all()

async def get_is_emri_operasyonu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(IsEmriOperasyonu).where(IsEmriOperasyonu.id == id))
    return result.scalar_one_or_none()

async def create_is_emri_operasyonu(db: AsyncSession, obj: IsEmriOperasyonu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj