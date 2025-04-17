from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_hareketi_03012025 import MalzemeHareketi03012025

async def get_all_malzeme_hareketi_03012025(db: AsyncSession):
    result = await db.execute(select(MalzemeHareketi03012025))
    return result.scalars().all()

async def get_malzeme_hareketi_03012025_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeHareketi03012025).where(MalzemeHareketi03012025.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_hareketi_03012025(db: AsyncSession, obj: MalzemeHareketi03012025):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj