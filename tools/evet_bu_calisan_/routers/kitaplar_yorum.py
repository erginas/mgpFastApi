from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.kitaplar_yorum import KitaplarYorum, KitaplarYorumCreate
from models.kitaplar_yorum import KitaplarYorum as DBKitaplarYorum
from crud.kitaplar_yorum import get_all_kitaplar_yorum, get_kitaplar_yorum_by_id, create_kitaplar_yorum

router = APIRouter(prefix='/kitaplar_yorum', tags=['KitaplarYorum'])

@router.get('/', response_model=list[KitaplarYorum])
async def list_kitaplar_yorum(db: AsyncSession = Depends()):
    return await get_all_kitaplar_yorum(db)

@router.get('/{id}', response_model=KitaplarYorum)
async def get_kitaplar_yorum_item(id: int, db: AsyncSession = Depends()):
    result = await get_kitaplar_yorum_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=KitaplarYorum)
async def create_kitaplar_yorum_item(data: KitaplarYorumCreate, db: AsyncSession = Depends()):
    db_item = DBKitaplarYorum(**data.dict())
    return await create_kitaplar_yorum(db, db_item)