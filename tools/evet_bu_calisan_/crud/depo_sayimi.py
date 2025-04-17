from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi import DepoSayimi

async def get_all_depo_sayimi(db: AsyncSession):
    result = await db.execute(select(DepoSayimi))
    return result.scalars().all()

async def get_depo_sayimi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi).where(DepoSayimi.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi(db: AsyncSession, obj: DepoSayimi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj