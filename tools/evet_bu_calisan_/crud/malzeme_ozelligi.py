from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_ozelligi import MalzemeOzelligi

async def get_all_malzeme_ozelligi(db: AsyncSession):
    result = await db.execute(select(MalzemeOzelligi))
    return result.scalars().all()

async def get_malzeme_ozelligi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeOzelligi).where(MalzemeOzelligi.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_ozelligi(db: AsyncSession, obj: MalzemeOzelligi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj