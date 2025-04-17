from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tezgah_kullanici import TezgahKullanici

async def get_all_tezgah_kullanici(db: AsyncSession):
    result = await db.execute(select(TezgahKullanici))
    return result.scalars().all()

async def get_tezgah_kullanici_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TezgahKullanici).where(TezgahKullanici.id == id))
    return result.scalar_one_or_none()

async def create_tezgah_kullanici(db: AsyncSession, obj: TezgahKullanici):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj