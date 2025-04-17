from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tpc_c_properties import TpcCProperties

async def get_all_tpc_c_properties(db: AsyncSession):
    result = await db.execute(select(TpcCProperties))
    return result.scalars().all()

async def get_tpc_c_properties_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TpcCProperties).where(TpcCProperties.id == id))
    return result.scalar_one_or_none()

async def create_tpc_c_properties(db: AsyncSession, obj: TpcCProperties):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj