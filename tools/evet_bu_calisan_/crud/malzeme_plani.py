from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_plani import MalzemePlani

async def get_all_malzeme_plani(db: AsyncSession):
    result = await db.execute(select(MalzemePlani))
    return result.scalars().all()

async def get_malzeme_plani_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemePlani).where(MalzemePlani.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_plani(db: AsyncSession, obj: MalzemePlani):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj