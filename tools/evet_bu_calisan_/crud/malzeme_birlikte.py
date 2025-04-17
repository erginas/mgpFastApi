from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_birlikte import MalzemeBirlikte

async def get_all_malzeme_birlikte(db: AsyncSession):
    result = await db.execute(select(MalzemeBirlikte))
    return result.scalars().all()

async def get_malzeme_birlikte_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeBirlikte).where(MalzemeBirlikte.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_birlikte(db: AsyncSession, obj: MalzemeBirlikte):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj