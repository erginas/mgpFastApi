from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.para_birimi import ParaBirimi

async def get_all_para_birimi(db: AsyncSession):
    result = await db.execute(select(ParaBirimi))
    return result.scalars().all()

async def get_para_birimi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ParaBirimi).where(ParaBirimi.id == id))
    return result.scalar_one_or_none()

async def create_para_birimi(db: AsyncSession, obj: ParaBirimi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj