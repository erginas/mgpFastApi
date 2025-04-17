from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.is_emri_reservesi import IsEmriReservesi

async def get_all_is_emri_reservesi(db: AsyncSession):
    result = await db.execute(select(IsEmriReservesi))
    return result.scalars().all()

async def get_is_emri_reservesi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(IsEmriReservesi).where(IsEmriReservesi.id == id))
    return result.scalar_one_or_none()

async def create_is_emri_reservesi(db: AsyncSession, obj: IsEmriReservesi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj