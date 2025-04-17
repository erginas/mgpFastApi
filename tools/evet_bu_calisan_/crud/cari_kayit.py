from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.cari_kayit import CariKayit

async def get_all_cari_kayit(db: AsyncSession):
    result = await db.execute(select(CariKayit))
    return result.scalars().all()

async def get_cari_kayit_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(CariKayit).where(CariKayit.id == id))
    return result.scalar_one_or_none()

async def create_cari_kayit(db: AsyncSession, obj: CariKayit):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj