from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tcks import Tcks

async def get_all_tcks(db: AsyncSession):
    result = await db.execute(select(Tcks))
    return result.scalars().all()

async def get_tcks_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Tcks).where(Tcks.id == id))
    return result.scalar_one_or_none()

async def create_tcks(db: AsyncSession, obj: Tcks):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj