from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sk_plan_olcusu import SkPlanOlcusu

async def get_all_sk_plan_olcusu(db: AsyncSession):
    result = await db.execute(select(SkPlanOlcusu))
    return result.scalars().all()

async def get_sk_plan_olcusu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SkPlanOlcusu).where(SkPlanOlcusu.id == id))
    return result.scalar_one_or_none()

async def create_sk_plan_olcusu(db: AsyncSession, obj: SkPlanOlcusu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj