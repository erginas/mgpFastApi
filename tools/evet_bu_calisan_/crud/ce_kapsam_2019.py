from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.ce_kapsam_2019 import CeKapsam2019

async def get_all_ce_kapsam_2019(db: AsyncSession):
    result = await db.execute(select(CeKapsam2019))
    return result.scalars().all()

async def get_ce_kapsam_2019_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(CeKapsam2019).where(CeKapsam2019.id == id))
    return result.scalar_one_or_none()

async def create_ce_kapsam_2019(db: AsyncSession, obj: CeKapsam2019):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj