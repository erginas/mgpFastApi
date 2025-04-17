from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tb_resim_tbl import TbResimTbl

async def get_all_tb_resim_tbl(db: AsyncSession):
    result = await db.execute(select(TbResimTbl))
    return result.scalars().all()

async def get_tb_resim_tbl_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TbResimTbl).where(TbResimTbl.id == id))
    return result.scalar_one_or_none()

async def create_tb_resim_tbl(db: AsyncSession, obj: TbResimTbl):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj