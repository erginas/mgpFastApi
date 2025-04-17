from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.hammadde_sertifika_referansi import HammaddeSertifikaReferansi

async def get_all_hammadde_sertifika_referansi(db: AsyncSession):
    result = await db.execute(select(HammaddeSertifikaReferansi))
    return result.scalars().all()

async def get_hammadde_sertifika_referansi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(HammaddeSertifikaReferansi).where(HammaddeSertifikaReferansi.id == id))
    return result.scalar_one_or_none()

async def create_hammadde_sertifika_referansi(db: AsyncSession, obj: HammaddeSertifikaReferansi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj