from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.django_content_type import DjangoContentType

async def get_all_django_content_type(db: AsyncSession):
    result = await db.execute(select(DjangoContentType))
    return result.scalars().all()

async def get_django_content_type_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(DjangoContentType).where(DjangoContentType.id == id))
    return result.scalar_one_or_none()

async def create_django_content_type(db: AsyncSession, obj: DjangoContentType):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj