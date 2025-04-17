from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme import Malzeme

async def get_all_malzeme(db: AsyncSession):
    result = await db.execute(select(Malzeme))
    return result.scalars().all()

async def get_malzeme_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Malzeme).where(Malzeme.id == id))
    return result.scalar_one_or_none()

async def create_malzeme(db: AsyncSession, obj: Malzeme):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj