from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.doviz_kuru import DovizKuru

async def get_all_doviz_kuru(db: AsyncSession):
    result = await db.execute(select(DovizKuru))
    return result.scalars().all()

async def get_doviz_kuru_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DovizKuru).where(DovizKuru.id == id))
    return result.scalar_one_or_none()

async def create_doviz_kuru(db: AsyncSession, obj: DovizKuru):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj