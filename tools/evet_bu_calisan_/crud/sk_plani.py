from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sk_plani import SkPlani

async def get_all_sk_plani(db: AsyncSession):
    result = await db.execute(select(SkPlani))
    return result.scalars().all()

async def get_sk_plani_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SkPlani).where(SkPlani.id == id))
    return result.scalar_one_or_none()

async def create_sk_plani(db: AsyncSession, obj: SkPlani):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj