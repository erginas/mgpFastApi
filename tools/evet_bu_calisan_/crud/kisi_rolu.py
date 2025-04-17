from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kisi_rolu import KisiRolu

async def get_all_kisi_rolu(db: AsyncSession):
    result = await db.execute(select(KisiRolu))
    return result.scalars().all()

async def get_kisi_rolu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(KisiRolu).where(KisiRolu.id == id))
    return result.scalar_one_or_none()

async def create_kisi_rolu(db: AsyncSession, obj: KisiRolu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj