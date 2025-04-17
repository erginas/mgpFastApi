from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.alinan_siparis_termin_takibi import AlinanSiparisTerminTakibi

async def get_all_alinan_siparis_termin_takibi(db: AsyncSession):
    result = await db.execute(select(AlinanSiparisTerminTakibi))
    return result.scalars().all()

async def get_alinan_siparis_termin_takibi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(AlinanSiparisTerminTakibi).where(AlinanSiparisTerminTakibi.id == id))
    return result.scalar_one_or_none()

async def create_alinan_siparis_termin_takibi(db: AsyncSession, obj: AlinanSiparisTerminTakibi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj