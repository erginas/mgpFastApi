from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.ariza_kaydi import ArizaKaydi

async def get_all_ariza_kaydi(db: AsyncSession):
    result = await db.execute(select(ArizaKaydi))
    return result.scalars().all()

async def get_ariza_kaydi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ArizaKaydi).where(ArizaKaydi.id == id))
    return result.scalar_one_or_none()

async def create_ariza_kaydi(db: AsyncSession, obj: ArizaKaydi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj