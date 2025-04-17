from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.huffman import Huffman, HuffmanCreate
from models.huffman import Huffman as DBHuffman
from crud.huffman import get_all_huffman, get_huffman_by_id, create_huffman

router = APIRouter(prefix='/huffman', tags=['Huffman'])

@router.get('/', response_model=list[Huffman])
async def list_huffman(db: AsyncSession = Depends()):
    return await get_all_huffman(db)

@router.get('/{id}', response_model=Huffman)
async def get_huffman_item(id: int, db: AsyncSession = Depends()):
    result = await get_huffman_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Huffman)
async def create_huffman_item(data: HuffmanCreate, db: AsyncSession = Depends()):
    db_item = DBHuffman(**data.dict())
    return await create_huffman(db, db_item)