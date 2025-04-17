from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.plan_donemi import PlanDonemi

async def get_all_plan_donemi(db: AsyncSession):
    result = await db.execute(select(PlanDonemi))
    return result.scalars().all()

async def get_plan_donemi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(PlanDonemi).where(PlanDonemi.id == id))
    return result.scalar_one_or_none()

async def create_plan_donemi(db: AsyncSession, obj: PlanDonemi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj