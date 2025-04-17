from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.izin_talebi import IzinTalebi

async def get_all_izin_talebi(db: AsyncSession):
    result = await db.execute(select(IzinTalebi))
    return result.scalars().all()

async def get_izin_talebi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(IzinTalebi).where(IzinTalebi.id == id))
    return result.scalar_one_or_none()

async def create_izin_talebi(db: AsyncSession, obj: IzinTalebi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj