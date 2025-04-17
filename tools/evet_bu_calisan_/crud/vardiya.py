from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.vardiya import Vardiya

async def get_all_vardiya(db: AsyncSession):
    result = await db.execute(select(Vardiya))
    return result.scalars().all()

async def get_vardiya_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Vardiya).where(Vardiya.id == id))
    return result.scalar_one_or_none()

async def create_vardiya(db: AsyncSession, obj: Vardiya):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj