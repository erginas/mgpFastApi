from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sayac_silinen import SayacSilinen, SayacSilinenCreate
from models.sayac_silinen import SayacSilinen as DBSayacSilinen
from crud.sayac_silinen import get_all_sayac_silinen, get_sayac_silinen_by_id, create_sayac_silinen

router = APIRouter(prefix='/sayac_silinen', tags=['SayacSilinen'])

@router.get('/', response_model=list[SayacSilinen])
async def list_sayac_silinen(db: AsyncSession = Depends()):
    return await get_all_sayac_silinen(db)

@router.get('/{id}', response_model=SayacSilinen)
async def get_sayac_silinen_item(id: int, db: AsyncSession = Depends()):
    result = await get_sayac_silinen_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SayacSilinen)
async def create_sayac_silinen_item(data: SayacSilinenCreate, db: AsyncSession = Depends()):
    db_item = DBSayacSilinen(**data.dict())
    return await create_sayac_silinen(db, db_item)