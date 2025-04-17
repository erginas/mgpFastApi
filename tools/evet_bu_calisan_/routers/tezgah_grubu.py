from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.tezgah_grubu import TezgahGrubu, TezgahGrubuCreate
from models.tezgah_grubu import TezgahGrubu as DBTezgahGrubu
from crud.tezgah_grubu import get_all_tezgah_grubu, get_tezgah_grubu_by_id, create_tezgah_grubu

router = APIRouter(prefix='/tezgah_grubu', tags=['TezgahGrubu'])

@router.get('/', response_model=list[TezgahGrubu])
async def list_tezgah_grubu(db: AsyncSession = Depends()):
    return await get_all_tezgah_grubu(db)

@router.get('/{id}', response_model=TezgahGrubu)
async def get_tezgah_grubu_item(id: int, db: AsyncSession = Depends()):
    result = await get_tezgah_grubu_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=TezgahGrubu)
async def create_tezgah_grubu_item(data: TezgahGrubuCreate, db: AsyncSession = Depends()):
    db_item = DBTezgahGrubu(**data.dict())
    return await create_tezgah_grubu(db, db_item)