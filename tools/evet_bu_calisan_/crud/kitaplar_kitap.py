from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kitaplar_kitap import KitaplarKitap

async def get_all_kitaplar_kitap(db: AsyncSession):
    result = await db.execute(select(KitaplarKitap))
    return result.scalars().all()

async def get_kitaplar_kitap_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(KitaplarKitap).where(KitaplarKitap.id == id))
    return result.scalar_one_or_none()

async def create_kitaplar_kitap(db: AsyncSession, obj: KitaplarKitap):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj