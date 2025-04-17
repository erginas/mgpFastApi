from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.resim_olcusu import ResimOlcusu

async def get_all_resim_olcusu(db: AsyncSession):
    result = await db.execute(select(ResimOlcusu))
    return result.scalars().all()

async def get_resim_olcusu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ResimOlcusu).where(ResimOlcusu.id == id))
    return result.scalar_one_or_none()

async def create_resim_olcusu(db: AsyncSession, obj: ResimOlcusu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj