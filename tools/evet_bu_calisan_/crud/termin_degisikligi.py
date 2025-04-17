from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.termin_degisikligi import TerminDegisikligi

async def get_all_termin_degisikligi(db: AsyncSession):
    result = await db.execute(select(TerminDegisikligi))
    return result.scalars().all()

async def get_termin_degisikligi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TerminDegisikligi).where(TerminDegisikligi.id == id))
    return result.scalar_one_or_none()

async def create_termin_degisikligi(db: AsyncSession, obj: TerminDegisikligi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj