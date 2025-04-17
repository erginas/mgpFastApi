from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.aktar_sut_fiyat2 import AktarSutFiyat2

async def get_all_aktar_sut_fiyat2(db: AsyncSession):
    result = await db.execute(select(AktarSutFiyat2))
    return result.scalars().all()

async def get_aktar_sut_fiyat2_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AktarSutFiyat2).where(AktarSutFiyat2.id == id))
    return result.scalar_one_or_none()

async def create_aktar_sut_fiyat2(db: AsyncSession, obj: AktarSutFiyat2):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj