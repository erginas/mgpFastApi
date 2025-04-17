from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.teknik_resim_kapsami import TeknikResimKapsami, TeknikResimKapsamiCreate
from models.teknik_resim_kapsami import TeknikResimKapsami as DBTeknikResimKapsami
from crud.teknik_resim_kapsami import get_all_teknik_resim_kapsami, get_teknik_resim_kapsami_by_id, create_teknik_resim_kapsami

router = APIRouter(prefix='/teknik_resim_kapsami', tags=['TeknikResimKapsami'])

@router.get('/', response_model=list[TeknikResimKapsami])
async def list_teknik_resim_kapsami(db: AsyncSession = Depends()):
    return await get_all_teknik_resim_kapsami(db)

@router.get('/{id}', response_model=TeknikResimKapsami)
async def get_teknik_resim_kapsami_item(id: int, db: AsyncSession = Depends()):
    result = await get_teknik_resim_kapsami_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TeknikResimKapsami)
async def create_teknik_resim_kapsami_item(data: TeknikResimKapsamiCreate, db: AsyncSession = Depends()):
    db_item = DBTeknikResimKapsami(**data.dict())
    return await create_teknik_resim_kapsami(db, db_item)