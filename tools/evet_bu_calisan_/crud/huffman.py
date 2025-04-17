from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.huffman import Huffman

async def get_all_huffman(db: AsyncSession):
    result = await db.execute(select(Huffman))
    return result.scalars().all()

async def get_huffman_by_id(db: AsyncSession, id: int):
    result = await db.execute(select(Huffman).where(Huffman.id == id))
    return result.scalar_one_or_none()

async def create_huffman(db: AsyncSession, obj: Huffman):
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj