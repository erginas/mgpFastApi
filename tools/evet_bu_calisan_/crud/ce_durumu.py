from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.ce_durumu import CeDurumu

async def get_all_ce_durumu(db: AsyncSession):
    result = await db.execute(select(CeDurumu))
    return result.scalars().all()

async def get_ce_durumu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(CeDurumu).where(CeDurumu.id == id))
    return result.scalar_one_or_none()

async def create_ce_durumu(db: AsyncSession, obj: CeDurumu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj