from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2004_07 import DepoSayimi200407

async def get_all_depo_sayimi_2004_07(db: AsyncSession):
    result = await db.execute(select(DepoSayimi200407))
    return result.scalars().all()

async def get_depo_sayimi_2004_07_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi200407).where(DepoSayimi200407.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2004_07(db: AsyncSession, obj: DepoSayimi200407):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj