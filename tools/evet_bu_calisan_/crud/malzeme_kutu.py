from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.malzeme_kutu import MalzemeKutu

async def get_all_malzeme_kutu(db: AsyncSession):
    result = await db.execute(select(MalzemeKutu))
    return result.scalars().all()

async def get_malzeme_kutu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MalzemeKutu).where(MalzemeKutu.id == id))
    return result.scalar_one_or_none()

async def create_malzeme_kutu(db: AsyncSession, obj: MalzemeKutu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj