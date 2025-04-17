from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.deleted_sakincali_lot import DeletedSakincaliLot

async def get_all_deleted_sakincali_lot(db: AsyncSession):
    result = await db.execute(select(DeletedSakincaliLot))
    return result.scalars().all()

async def get_deleted_sakincali_lot_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DeletedSakincaliLot).where(DeletedSakincaliLot.id == id))
    return result.scalar_one_or_none()

async def create_deleted_sakincali_lot(db: AsyncSession, obj: DeletedSakincaliLot):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj