from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.toplanti_ilgilisi import ToplantiIlgilisi

async def get_all_toplanti_ilgilisi(db: AsyncSession):
    result = await db.execute(select(ToplantiIlgilisi))
    return result.scalars().all()

async def get_toplanti_ilgilisi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(ToplantiIlgilisi).where(ToplantiIlgilisi.id == id))
    return result.scalar_one_or_none()

async def create_toplanti_ilgilisi(db: AsyncSession, obj: ToplantiIlgilisi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj