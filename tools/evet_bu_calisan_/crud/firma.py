from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.firma import Firma

async def get_all_firma(db: AsyncSession):
    result = await db.execute(select(Firma))
    return result.scalars().all()

async def get_firma_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Firma).where(Firma.id == id))
    return result.scalar_one_or_none()

async def create_firma(db: AsyncSession, obj: Firma):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj