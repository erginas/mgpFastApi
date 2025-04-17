from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.is_emri_operasyon_durusu import IsEmriOperasyonDurusu

async def get_all_is_emri_operasyon_durusu(db: AsyncSession):
    result = await db.execute(select(IsEmriOperasyonDurusu))
    return result.scalars().all()

async def get_is_emri_operasyon_durusu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(IsEmriOperasyonDurusu).where(IsEmriOperasyonDurusu.id == id))
    return result.scalar_one_or_none()

async def create_is_emri_operasyon_durusu(db: AsyncSession, obj: IsEmriOperasyonDurusu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj