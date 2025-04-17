from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.ameliyat_ekibi import AmeliyatEkibi

async def get_all_ameliyat_ekibi(db: AsyncSession):
    result = await db.execute(select(AmeliyatEkibi))
    return result.scalars().all()

async def get_ameliyat_ekibi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AmeliyatEkibi).where(AmeliyatEkibi.id == id))
    return result.scalar_one_or_none()

async def create_ameliyat_ekibi(db: AsyncSession, obj: AmeliyatEkibi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj