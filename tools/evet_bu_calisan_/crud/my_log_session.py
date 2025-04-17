from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.my_log_session import MyLogSession

async def get_all_my_log_session(db: AsyncSession):
    result = await db.execute(select(MyLogSession))
    return result.scalars().all()

async def get_my_log_session_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(MyLogSession).where(MyLogSession.id == id))
    return result.scalar_one_or_none()

async def create_my_log_session(db: AsyncSession, obj: MyLogSession):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj