from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.siparis_sevk_kolisi import SiparisSevkKolisi

async def get_all_siparis_sevk_kolisi(db: AsyncSession):
    result = await db.execute(select(SiparisSevkKolisi))
    return result.scalars().all()

async def get_siparis_sevk_kolisi_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(SiparisSevkKolisi).where(SiparisSevkKolisi.id == id))
    return result.scalar_one_or_none()

async def create_siparis_sevk_kolisi(db: AsyncSession, obj: SiparisSevkKolisi):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj