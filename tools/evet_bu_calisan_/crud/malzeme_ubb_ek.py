from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_ubb_ek import MalzemeUbbEk

async def get_all_malzeme_ubb_ek(db: AsyncSession):
    result = await db.execute(select(MalzemeUbbEk))
    return result.scalars().all()

async def get_malzeme_ubb_ek_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeUbbEk).where(MalzemeUbbEk.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_ubb_ek(db: AsyncSession, obj: MalzemeUbbEk):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj