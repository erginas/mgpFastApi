from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_set import MalzemeSet

async def get_all_malzeme_set(db: AsyncSession):
    result = await db.execute(select(MalzemeSet))
    return result.scalars().all()

async def get_malzeme_set_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeSet).where(MalzemeSet.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_set(db: AsyncSession, obj: MalzemeSet):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj