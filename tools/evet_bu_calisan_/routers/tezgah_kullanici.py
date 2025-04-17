from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tezgah_kullanici import TezgahKullanici, TezgahKullaniciCreate
from models.tezgah_kullanici import TezgahKullanici as DBTezgahKullanici
from crud.tezgah_kullanici import get_all_tezgah_kullanici, get_tezgah_kullanici_by_id, create_tezgah_kullanici

router = APIRouter(prefix='/tezgah_kullanici', tags=['TezgahKullanici'])

@router.get('/', response_model=list[TezgahKullanici])
async def list_tezgah_kullanici(db: AsyncSession = Depends()):
    return await get_all_tezgah_kullanici(db)

@router.get('/{id}', response_model=TezgahKullanici)
async def get_tezgah_kullanici_item(id: int, db: AsyncSession = Depends()):
    result = await get_tezgah_kullanici_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TezgahKullanici)
async def create_tezgah_kullanici_item(data: TezgahKullaniciCreate, db: AsyncSession = Depends()):
    db_item = DBTezgahKullanici(**data.dict())
    return await create_tezgah_kullanici(db, db_item)