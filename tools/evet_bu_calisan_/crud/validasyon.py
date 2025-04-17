from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.validasyon import Validasyon

async def get_all_validasyon(db: AsyncSession):
    result = await db.execute(select(Validasyon))
    return result.scalars().all()

async def get_validasyon_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Validasyon).where(Validasyon.id == id))
    return result.scalar_one_or_none()

async def create_validasyon(db: AsyncSession, obj: Validasyon):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj