from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tmp_resim_olcusu import TmpResimOlcusu

async def get_all_tmp_resim_olcusu(db: AsyncSession):
    result = await db.execute(select(TmpResimOlcusu))
    return result.scalars().all()

async def get_tmp_resim_olcusu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TmpResimOlcusu).where(TmpResimOlcusu.id == id))
    return result.scalar_one_or_none()

async def create_tmp_resim_olcusu(db: AsyncSession, obj: TmpResimOlcusu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj