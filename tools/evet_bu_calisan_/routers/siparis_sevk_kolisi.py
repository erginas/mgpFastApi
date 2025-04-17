from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.siparis_sevk_kolisi import SiparisSevkKolisi, SiparisSevkKolisiCreate
from models.siparis_sevk_kolisi import SiparisSevkKolisi as DBSiparisSevkKolisi
from crud.siparis_sevk_kolisi import get_all_siparis_sevk_kolisi, get_siparis_sevk_kolisi_by_id, create_siparis_sevk_kolisi

router = APIRouter(prefix='/siparis_sevk_kolisi', tags=['SiparisSevkKolisi'])

@router.get('/', response_model=list[SiparisSevkKolisi])
async def list_siparis_sevk_kolisi(db: AsyncSession = Depends()):
    return await get_all_siparis_sevk_kolisi(db)

@router.get('/{id}', response_model=SiparisSevkKolisi)
async def get_siparis_sevk_kolisi_item(id: int, db: AsyncSession = Depends()):
    result = await get_siparis_sevk_kolisi_by_id(db, id)
    if not result: raise HTTPException(404, detail='Not found')
    return result

@router.post('/', response_model=SiparisSevkKolisi)
async def create_siparis_sevk_kolisi_item(data: SiparisSevkKolisiCreate, db: AsyncSession = Depends()):
    db_item = DBSiparisSevkKolisi(**data.dict())
    return await create_siparis_sevk_kolisi(db, db_item)