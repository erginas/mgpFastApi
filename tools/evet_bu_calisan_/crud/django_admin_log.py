from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.django_admin_log import DjangoAdminLog

async def get_all_django_admin_log(db: AsyncSession):
    result = await db.execute(select(DjangoAdminLog))
    return result.scalars().all()

async def get_django_admin_log_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DjangoAdminLog).where(DjangoAdminLog.id == id))
    return result.scalar_one_or_none()

async def create_django_admin_log(db: AsyncSession, obj: DjangoAdminLog):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj