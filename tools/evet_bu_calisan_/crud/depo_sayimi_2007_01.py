from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2007_01 import DepoSayimi200701

async def get_all_depo_sayimi_2007_01(db: AsyncSession):
    result = await db.execute(select(DepoSayimi200701))
    return result.scalars().all()

async def get_depo_sayimi_2007_01_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi200701).where(DepoSayimi200701.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2007_01(db: AsyncSession, obj: DepoSayimi200701):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj