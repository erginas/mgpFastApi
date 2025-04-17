from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.ubb_transfer import UbbTransfer

async def get_all_ubb_transfer(db: AsyncSession):
    result = await db.execute(select(UbbTransfer))
    return result.scalars().all()

async def get_ubb_transfer_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(UbbTransfer).where(UbbTransfer.id == id))
    return result.scalar_one_or_none()

async def create_ubb_transfer(db: AsyncSession, obj: UbbTransfer):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj