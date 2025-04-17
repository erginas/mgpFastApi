from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_birimi import MalzemeBirimi

async def get_all_malzeme_birimi(db: AsyncSession):
    result = await db.execute(select(MalzemeBirimi))
    return result.scalars().all()

async def get_malzeme_birimi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeBirimi).where(MalzemeBirimi.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_birimi(db: AsyncSession, obj: MalzemeBirimi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj