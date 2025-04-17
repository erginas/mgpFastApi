from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.depo_sayimi_2025_01_ha import DepoSayimi202501Ha

async def get_all_depo_sayimi_2025_01_ha(db: AsyncSession):
    result = await db.execute(select(DepoSayimi202501Ha))
    return result.scalars().all()

async def get_depo_sayimi_2025_01_ha_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DepoSayimi202501Ha).where(DepoSayimi202501Ha.id == id))
    return result.scalar_one_or_none()

async def create_depo_sayimi_2025_01_ha(db: AsyncSession, obj: DepoSayimi202501Ha):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj