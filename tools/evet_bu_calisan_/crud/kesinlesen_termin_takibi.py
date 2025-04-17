from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kesinlesen_termin_takibi import KesinlesenTerminTakibi

async def get_all_kesinlesen_termin_takibi(db: AsyncSession):
    result = await db.execute(select(KesinlesenTerminTakibi))
    return result.scalars().all()

async def get_kesinlesen_termin_takibi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(KesinlesenTerminTakibi).where(KesinlesenTerminTakibi.id == id))
    return result.scalar_one_or_none()

async def create_kesinlesen_termin_takibi(db: AsyncSession, obj: KesinlesenTerminTakibi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj