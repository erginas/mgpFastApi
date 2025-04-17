from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.malzeme_recete import MalzemeRecete, MalzemeReceteCreate
from models.malzeme_recete import MalzemeRecete as DBMalzemeRecete
from crud.malzeme_recete import get_all_malzeme_recete, get_malzeme_recete_by_id, create_malzeme_recete

router = APIRouter(prefix='/malzeme_recete', tags=['MalzemeRecete'])

@router.get('/', response_model=list[MalzemeRecete])
async def list_malzeme_recete(db: AsyncSession = Depends()):
    return await get_all_malzeme_recete(db)

@router.get('/{id}', response_model=MalzemeRecete)
async def get_malzeme_recete_item(id: int, db: AsyncSession = Depends()):
    result = await get_malzeme_recete_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=MalzemeRecete)
async def create_malzeme_recete_item(data: MalzemeReceteCreate, db: AsyncSession = Depends()):
    db_item = DBMalzemeRecete(**data.dict())
    return await create_malzeme_recete(db, db_item)