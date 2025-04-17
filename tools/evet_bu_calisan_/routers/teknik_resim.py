from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.teknik_resim import TeknikResim, TeknikResimCreate
from models.teknik_resim import TeknikResim as DBTeknikResim
from crud.teknik_resim import get_all_teknik_resim, get_teknik_resim_by_id, create_teknik_resim

router = APIRouter(prefix='/teknik_resim', tags=['TeknikResim'])

@router.get('/', response_model=list[TeknikResim])
async def list_teknik_resim(db: AsyncSession = Depends()):
    return await get_all_teknik_resim(db)

@router.get('/{id}', response_model=TeknikResim)
async def get_teknik_resim_item(id: int, db: AsyncSession = Depends()):
    result = await get_teknik_resim_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TeknikResim)
async def create_teknik_resim_item(data: TeknikResimCreate, db: AsyncSession = Depends()):
    db_item = DBTeknikResim(**data.dict())
    return await create_teknik_resim(db, db_item)