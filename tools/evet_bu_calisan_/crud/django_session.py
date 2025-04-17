from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.django_session import DjangoSession

async def get_all_django_session(db: AsyncSession):
    result = await db.execute(select(DjangoSession))
    return result.scalars().all()

async def get_django_session_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DjangoSession).where(DjangoSession.id == id))
    return result.scalar_one_or_none()

async def create_django_session(db: AsyncSession, obj: DjangoSession):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj