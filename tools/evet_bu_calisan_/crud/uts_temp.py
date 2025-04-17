from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uts_temp import UtsTemp

async def get_all_uts_temp(db: AsyncSession):
    result = await db.execute(select(UtsTemp))
    return result.scalars().all()

async def get_uts_temp_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UtsTemp).where(UtsTemp.id == id))
    return result.scalar_one_or_none()

async def create_uts_temp(db: AsyncSession, obj: UtsTemp):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj