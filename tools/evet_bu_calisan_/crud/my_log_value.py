from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.my_log_value import MyLogValue

async def get_all_my_log_value(db: AsyncSession):
    result = await db.execute(select(MyLogValue))
    return result.scalars().all()

async def get_my_log_value_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MyLogValue).where(MyLogValue.id == id))
    return result.scalar_one_or_none()

async def create_my_log_value(db: AsyncSession, obj: MyLogValue):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj