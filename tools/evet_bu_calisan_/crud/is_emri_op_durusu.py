from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.is_emri_op_durusu import IsEmriOpDurusu

async def get_all_is_emri_op_durusu(db: AsyncSession):
    result = await db.execute(select(IsEmriOpDurusu))
    return result.scalars().all()

async def get_is_emri_op_durusu_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(IsEmriOpDurusu).where(IsEmriOpDurusu.id == id))
    return result.scalar_one_or_none()

async def create_is_emri_op_durusu(db: AsyncSession, obj: IsEmriOpDurusu):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj