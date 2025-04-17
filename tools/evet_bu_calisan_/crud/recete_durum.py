from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.recete_durum import ReceteDurum

async def get_all_recete_durum(db: AsyncSession):
    result = await db.execute(select(ReceteDurum))
    return result.scalars().all()

async def get_recete_durum_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ReceteDurum).where(ReceteDurum.id == id))
    return result.scalar_one_or_none()

async def create_recete_durum(db: AsyncSession, obj: ReceteDurum):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj