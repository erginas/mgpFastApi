from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_hareketi import MalzemeHareketi

async def get_all_malzeme_hareketi(db: AsyncSession):
    result = await db.execute(select(MalzemeHareketi))
    return result.scalars().all()

async def get_malzeme_hareketi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeHareketi).where(MalzemeHareketi.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_hareketi(db: AsyncSession, obj: MalzemeHareketi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj