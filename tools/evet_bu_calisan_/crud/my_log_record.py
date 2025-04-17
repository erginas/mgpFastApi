from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.my_log_record import MyLogRecord

async def get_all_my_log_record(db: AsyncSession):
    result = await db.execute(select(MyLogRecord))
    return result.scalars().all()

async def get_my_log_record_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MyLogRecord).where(MyLogRecord.id == id))
    return result.scalar_one_or_none()

async def create_my_log_record(db: AsyncSession, obj: MyLogRecord):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj