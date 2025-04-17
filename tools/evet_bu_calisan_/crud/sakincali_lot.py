from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.sakincali_lot import SakincaliLot

async def get_all_sakincali_lot(db: AsyncSession):
    result = await db.execute(select(SakincaliLot))
    return result.scalars().all()

async def get_sakincali_lot_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SakincaliLot).where(SakincaliLot.id == id))
    return result.scalar_one_or_none()

async def create_sakincali_lot(db: AsyncSession, obj: SakincaliLot):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj