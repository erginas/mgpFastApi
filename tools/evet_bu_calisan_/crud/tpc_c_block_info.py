from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.tpc_c_block_info import TpcCBlockInfo

async def get_all_tpc_c_block_info(db: AsyncSession):
    result = await db.execute(select(TpcCBlockInfo))
    return result.scalars().all()

async def get_tpc_c_block_info_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(TpcCBlockInfo).where(TpcCBlockInfo.id == id))
    return result.scalar_one_or_none()

async def create_tpc_c_block_info(db: AsyncSession, obj: TpcCBlockInfo):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj