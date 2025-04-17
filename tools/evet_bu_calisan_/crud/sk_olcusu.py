from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sk_olcusu import SkOlcusu

async def get_all_sk_olcusu(db: AsyncSession):
    result = await db.execute(select(SkOlcusu))
    return result.scalars().all()

async def get_sk_olcusu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SkOlcusu).where(SkOlcusu.id == id))
    return result.scalar_one_or_none()

async def create_sk_olcusu(db: AsyncSession, obj: SkOlcusu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj