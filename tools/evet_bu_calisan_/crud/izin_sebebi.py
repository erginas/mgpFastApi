from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.izin_sebebi import IzinSebebi

async def get_all_izin_sebebi(db: AsyncSession):
    result = await db.execute(select(IzinSebebi))
    return result.scalars().all()

async def get_izin_sebebi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(IzinSebebi).where(IzinSebebi.id == id))
    return result.scalar_one_or_none()

async def create_izin_sebebi(db: AsyncSession, obj: IzinSebebi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj