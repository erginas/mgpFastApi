from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .huffman2_service import merhaba_get, encode_barkod, decode_barkod, huffman_service

router = APIRouter()

@router.get("/merhaba")
async def merhaba_endpoint():
    return await merhaba_get()


class DecodeRequest(BaseModel):
    barcode: str  # JSON body'den gelecek alan

@router.post("/decode")
async def decode_barkod(request: DecodeRequest):
    try:
        result = await huffman_service.decode_barkod(request.barcode)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

class BarcodeRequest(BaseModel):
    stokKodu: str
    opsn: str
    lotNo: str
    skt: Optional[datetime] = None  # Tarih opsiyonel
    ce: bool = False  # Varsayılan False

@router.post("/encode")
async def encode_barkod(request: BarcodeRequest):
    try:
        barkod = await huffman_service.encode_barkod(
            request.stokKodu,
            request.opsn,
            request.lotNo,
            request.skt,
            request.ce
        )
        return {"barkod": barkod}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

