from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.firma_siniflandirmasi import FirmaSiniflandirmasi

async def get_all_firma_siniflandirmasi(db: AsyncSession):
    result = await db.execute(select(FirmaSiniflandirmasi))
    return result.scalars().all()

async def get_firma_siniflandirmasi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(FirmaSiniflandirmasi).where(FirmaSiniflandirmasi.id == id))
    return result.scalar_one_or_none()

async def create_firma_siniflandirmasi(db: AsyncSession, obj: FirmaSiniflandirmasi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj