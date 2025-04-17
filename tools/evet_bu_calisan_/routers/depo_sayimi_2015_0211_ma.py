from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.depo_sayimi_2015_0211_ma import DepoSayimi20150211Ma, DepoSayimi20150211MaCreate
from models.depo_sayimi_2015_0211_ma import DepoSayimi20150211Ma as DBDepoSayimi20150211Ma
from crud.depo_sayimi_2015_0211_ma import get_all_depo_sayimi_2015_0211_ma, get_depo_sayimi_2015_0211_ma_by_id, create_depo_sayimi_2015_0211_ma

router = APIRouter(prefix='/depo_sayimi_2015_0211_ma', tags=['DepoSayimi20150211Ma'])

@router.get('/', response_model=list[DepoSayimi20150211Ma])
async def list_depo_sayimi_2015_0211_ma(db: AsyncSession = Depends()):
    return await get_all_depo_sayimi_2015_0211_ma(db)

@router.get('/{id}', response_model=DepoSayimi20150211Ma)
async def get_depo_sayimi_2015_0211_ma_item(id: int, db: AsyncSession = Depends()):
    result = await get_depo_sayimi_2015_0211_ma_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=DepoSayimi20150211Ma)
async def create_depo_sayimi_2015_0211_ma_item(data: DepoSayimi20150211MaCreate, db: AsyncSession = Depends()):
    db_item = DBDepoSayimi20150211Ma(**data.dict())
    return await create_depo_sayimi_2015_0211_ma(db, db_item)