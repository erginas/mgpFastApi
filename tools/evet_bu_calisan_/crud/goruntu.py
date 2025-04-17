from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.goruntu import Goruntu

async def get_all_goruntu(db: AsyncSession):
    result = await db.execute(select(Goruntu))
    return result.scalars().all()

async def get_goruntu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Goruntu).where(Goruntu.id == id))
    return result.scalar_one_or_none()

async def create_goruntu(db: AsyncSession, obj: Goruntu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj