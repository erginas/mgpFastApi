from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.uretim_tuketim import UretimTuketim

async def get_all_uretim_tuketim(db: AsyncSession):
    result = await db.execute(select(UretimTuketim))
    return result.scalars().all()

async def get_uretim_tuketim_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UretimTuketim).where(UretimTuketim.id == id))
    return result.scalar_one_or_none()

async def create_uretim_tuketim(db: AsyncSession, obj: UretimTuketim):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj