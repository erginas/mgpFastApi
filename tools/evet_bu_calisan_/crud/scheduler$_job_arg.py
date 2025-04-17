from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.scheduler$_job_arg import Scheduler$JobArg

async def get_all_scheduler$_job_arg(db: AsyncSession):
    result = await db.execute(select(Scheduler$JobArg))
    return result.scalars().all()

async def get_scheduler$_job_arg_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Scheduler$JobArg).where(Scheduler$JobArg.id == id))
    return result.scalar_one_or_none()

async def create_scheduler$_job_arg(db: AsyncSession, obj: Scheduler$JobArg):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj