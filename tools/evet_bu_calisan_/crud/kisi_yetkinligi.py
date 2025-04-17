from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kisi_yetkinligi import KisiYetkinligi

async def get_all_kisi_yetkinligi(db: AsyncSession):
    result = await db.execute(select(KisiYetkinligi))
    return result.scalars().all()

async def get_kisi_yetkinligi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(KisiYetkinligi).where(KisiYetkinligi.id == id))
    return result.scalar_one_or_none()

async def create_kisi_yetkinligi(db: AsyncSession, obj: KisiYetkinligi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj