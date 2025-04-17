from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.aktar_sut_fiyat import AktarSutFiyat

async def get_all_aktar_sut_fiyat(db: AsyncSession):
    result = await db.execute(select(AktarSutFiyat))
    return result.scalars().all()

async def get_aktar_sut_fiyat_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AktarSutFiyat).where(AktarSutFiyat.id == id))
    return result.scalar_one_or_none()

async def create_aktar_sut_fiyat(db: AsyncSession, obj: AktarSutFiyat):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj