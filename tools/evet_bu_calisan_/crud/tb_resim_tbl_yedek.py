from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tb_resim_tbl_yedek import TbResimTblYedek

async def get_all_tb_resim_tbl_yedek(db: AsyncSession):
    result = await db.execute(select(TbResimTblYedek))
    return result.scalars().all()

async def get_tb_resim_tbl_yedek_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TbResimTblYedek).where(TbResimTblYedek.id == id))
    return result.scalar_one_or_none()

async def create_tb_resim_tbl_yedek(db: AsyncSession, obj: TbResimTblYedek):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj