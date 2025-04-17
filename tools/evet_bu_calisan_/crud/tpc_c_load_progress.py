from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tpc_c_load_progress import TpcCLoadProgress

async def get_all_tpc_c_load_progress(db: AsyncSession):
    result = await db.execute(select(TpcCLoadProgress))
    return result.scalars().all()

async def get_tpc_c_load_progress_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TpcCLoadProgress).where(TpcCLoadProgress.id == id))
    return result.scalar_one_or_none()

async def create_tpc_c_load_progress(db: AsyncSession, obj: TpcCLoadProgress):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj