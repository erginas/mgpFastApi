from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kontrol_prefix import KontrolPrefix

async def get_all_kontrol_prefix(db: AsyncSession):
    result = await db.execute(select(KontrolPrefix))
    return result.scalars().all()

async def get_kontrol_prefix_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(KontrolPrefix).where(KontrolPrefix.id == id))
    return result.scalar_one_or_none()

async def create_kontrol_prefix(db: AsyncSession, obj: KontrolPrefix):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj