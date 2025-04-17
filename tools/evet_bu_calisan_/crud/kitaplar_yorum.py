from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kitaplar_yorum import KitaplarYorum

async def get_all_kitaplar_yorum(db: AsyncSession):
    result = await db.execute(select(KitaplarYorum))
    return result.scalars().all()

async def get_kitaplar_yorum_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(KitaplarYorum).where(KitaplarYorum.id == id))
    return result.scalar_one_or_none()

async def create_kitaplar_yorum(db: AsyncSession, obj: KitaplarYorum):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj