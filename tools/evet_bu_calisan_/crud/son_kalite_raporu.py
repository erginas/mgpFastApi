from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.son_kalite_raporu import SonKaliteRaporu

async def get_all_son_kalite_raporu(db: AsyncSession):
    result = await db.execute(select(SonKaliteRaporu))
    return result.scalars().all()

async def get_son_kalite_raporu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SonKaliteRaporu).where(SonKaliteRaporu.id == id))
    return result.scalar_one_or_none()

async def create_son_kalite_raporu(db: AsyncSession, obj: SonKaliteRaporu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj