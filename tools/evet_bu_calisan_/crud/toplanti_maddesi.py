from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.toplanti_maddesi import ToplantiMaddesi

async def get_all_toplanti_maddesi(db: AsyncSession):
    result = await db.execute(select(ToplantiMaddesi))
    return result.scalars().all()

async def get_toplanti_maddesi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ToplantiMaddesi).where(ToplantiMaddesi.id == id))
    return result.scalar_one_or_none()

async def create_toplanti_maddesi(db: AsyncSession, obj: ToplantiMaddesi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj