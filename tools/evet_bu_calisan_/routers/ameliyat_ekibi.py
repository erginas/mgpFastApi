from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.ameliyat_ekibi import AmeliyatEkibi, AmeliyatEkibiCreate
from models.ameliyat_ekibi import AmeliyatEkibi as DBAmeliyatEkibi
from crud.ameliyat_ekibi import get_all_ameliyat_ekibi, get_ameliyat_ekibi_by_id, create_ameliyat_ekibi

router = APIRouter(prefix='/ameliyat_ekibi', tags=['AmeliyatEkibi'])

@router.get('/', response_model=list[AmeliyatEkibi])
async def list_ameliyat_ekibi(db: AsyncSession = Depends()):
    return await get_all_ameliyat_ekibi(db)

@router.get('/{id}', response_model=AmeliyatEkibi)
async def get_ameliyat_ekibi_item(id: int, db: AsyncSession = Depends()):
    result = await get_ameliyat_ekibi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=AmeliyatEkibi)
async def create_ameliyat_ekibi_item(data: AmeliyatEkibiCreate, db: AsyncSession = Depends()):
    db_item = DBAmeliyatEkibi(**data.dict())
    return await create_ameliyat_ekibi(db, db_item)