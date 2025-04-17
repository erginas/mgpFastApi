from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.sayac import Sayac, SayacCreate
from models.sayac import Sayac as DBSayac
from crud.sayac import get_all_sayac, get_sayac_by_id, create_sayac

router = APIRouter(prefix='/sayac', tags=['Sayac'])

@router.get('/', response_model=list[Sayac])
async def list_sayac(db: AsyncSession = Depends()):
    return await get_all_sayac(db)

@router.get('/{id}', response_model=Sayac)
async def get_sayac_item(id: int, db: AsyncSession = Depends()):
    result = await get_sayac_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=Sayac)
async def create_sayac_item(data: SayacCreate, db: AsyncSession = Depends()):
    db_item = DBSayac(**data.dict())
    return await create_sayac(db, db_item)