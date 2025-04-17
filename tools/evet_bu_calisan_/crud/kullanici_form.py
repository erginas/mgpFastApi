from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.kullanici_form import KullaniciForm

async def get_all_kullanici_form(db: AsyncSession):
    result = await db.execute(select(KullaniciForm))
    return result.scalars().all()

async def get_kullanici_form_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(KullaniciForm).where(KullaniciForm.id == id))
    return result.scalar_one_or_none()

async def create_kullanici_form(db: AsyncSession, obj: KullaniciForm):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj