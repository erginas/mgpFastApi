from fastapi import APIRouter, HTTPException, FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

# router = APIRouter()

app = FastAPI()

HUFFMAN_TABLE = [
    {"key": "+0+", "value": "00"},
    {"key": "+1+", "value": "01"},
    {"key": "+2+", "value": "10000"},
    {"key": "+3+", "value": "10001"},
    {"key": "+6+", "value": "10010"},
    {"key": "+~+", "value": "10011"},
    {"key": "+@+", "value": "10100"},
    {"key": "+£+", "value": "10101"},
    {"key": "+8+", "value": "10110"},
    {"key": "+5+", "value": "10111"},
    {"key": "+4+", "value": "11000"},
    {"key": "+7+", "value": "11001"},
    {"key": "+.+", "value": "11010000"},
    {"key": "+9+", "value": "11010001"},
    {"key": "+A+", "value": "11010010"},
    {"key": "+$+", "value": "11010011"},
    {"key": "+B+", "value": "11010100"},
    {"key": "+J+", "value": "11010101"},
    {"key": "+C+", "value": "11010110"},
    {"key": "+E+", "value": "11010111"},
    {"key": "+F+", "value": "11011000"},
    {"key": "+Y+", "value": "11011001"},
    {"key": "+D+", "value": "11011010"},
    {"key": "+S+", "value": "11011011"},
    {"key": "+H+", "value": "11011100"},
    {"key": "+U+", "value": "11011101"},
    {"key": "+G+", "value": "11011110"},
    {"key": "+M+", "value": "11011111"},
    {"key": "+-+", "value": "11100000"},
    {"key": "+T+", "value": "11100001"},
    {"key": "+O+", "value": "11100010"},
    {"key": "+Z+", "value": "11100011"},
    {"key": "+L+", "value": "11100100"},
    {"key": "+K+", "value": "11100101"},
    {"key": "+/+", "value": "11100110"},
    {"key": "+=+", "value": "11100111"},
    {"key": "+*+", "value": "11101000"},
    {"key": "+?+", "value": "11101001"},
    {"key": "+N+", "value": "11101010"},
    {"key": "+P+", "value": "11101011"},
    {"key": "+I+", "value": "11101100"},
    {"key": "+R+", "value": "11101101"},
    {"key": "+X+", "value": "11101110"},
    {"key": "+W+", "value": "11101111"},
    {"key": "+V+", "value": "11110000"},
    {"key": "+Q+", "value": "11110001"},
    {"key": "+:+", "value": "11110010"},
    {"key": "+(+", "value": "11110011"},
    {"key": "+)+", "value": "11110100"},
    {"key": "+;+", "value": "11110101"},
    {"key": "+_+", "value": "11110110"},
    {"key": "+&+", "value": "11110111"},
    {"key": "+%+", "value": "11111000"},
    {"key": "+,+", "value": "11111001"},
    {"key": "+!+", "value": "11111010"},
    {"key": "+++", "value": "11111011"},
    {"key": "+ +", "value": "11111100"},
    {"key": "+ý+", "value": "11111101"},
    {"key": "+ü+", "value": "11111110"},
]

class BarcodeRequest(BaseModel):
    stokKodu: str
    opsn: str
    lotNo: str
    skt: Optional[str] = None
    ce: bool = False

class DecodeRequest(BaseModel):
    barkod: str

class HuffmanService:
    def __init__(self):
        self.huffman_map = {item["key"]: item["value"] for item in HUFFMAN_TABLE}
        self.reverse_huffman = {item["value"]: item["key"] for item in HUFFMAN_TABLE}

    async def encode(self, data: str) -> str:
        result = ''
        for char in data:
            item = next((x for x in HUFFMAN_TABLE if x["key"] == f"+{char}+"), None)
            if item:
                result += item["value"]
        return result

    @staticmethod
    def bin_to_dec(bin_str: str) -> int:
        return int(bin_str, 2)

    @staticmethod
    def dec_to_bin(dec: int, length: int) -> str:
        return bin(dec)[2:].zfill(length)

    async def huffman_sifrele(self, xs: str) -> str:
        txt = ''
        for char in xs:
            kod = f"+{char}+"
            value = self.huffman_map.get(kod)
            if not value:
                return ''
            txt += value

        deger = ''
        while txt:
            chunk = txt[:3]
            txt = txt[3:]
            if len(chunk) == 1:
                deger += '9' + str(self.bin_to_dec(chunk))
            elif len(chunk) == 2:
                deger += '8' + str(self.bin_to_dec(chunk))
            else:
                deger += str(self.bin_to_dec(chunk))

        uz = len(deger)
        if uz % 2 != 0:
            deger += '9'
        return deger

    async def huffman_sifre_coz(self, xs: str) -> str:
        if not xs.isdigit():
            return ''

        if xs.endswith('9'):
            xs = xs[:-1]

        txt = ''
        i = 0
        while i < len(xs):
            dgr = int(xs[i])
            if dgr < 8:
                txt += self.dec_to_bin(dgr, 3)
                i += 1
            else:
                if i + 1 >= len(xs):
                    return ''
                kontrol = xs[i+1]
                txt += self.dec_to_bin(int(kontrol), 2 if dgr == 8 else 1)
                i += 2

        dd = ''
        while txt:
            found = False
            for code, key in self.reverse_huffman.items():
                if txt.startswith(code):
                    dd += key[1]  # +A+ -> A
                    txt = txt[len(code):]
                    found = True
                    break
            if not found:
                if txt != '0':
                    return ''
                break
        return dd

    async def encode_barkod(self, stokKodu: str, opsn: str, lotNo: str, skt: Optional[str] = None, ce: bool = False) -> str:
        date_part = ''
        if skt:
            dt = datetime.strptime(skt, "%Y-%m-%d")
            date_part = '$' + dt.strftime('%y%m')
        return await self.huffman_sifrele(f"{stokKodu}@{opsn}~{lotNo}{date_part}{'£' if ce else ''}")

    async def decode_barkod(self, barkod: str) -> Dict[str, Any]:
        decoded = await self.huffman_sifre_coz(barkod)
        if not decoded:
            raise ValueError("Geçersiz barkod")

        parts = decoded.split('@')
        if len(parts) != 2:
            raise ValueError("Geçersiz barkod formatı")

        stokKodu = parts[0]
        parts2 = parts[1].split('~')
        if len(parts2) != 2:
            raise ValueError("Geçersiz barkod formatı")

        opsn = parts2[0]
        parts3 = parts2[1].split('$')
        lotNo = parts3[0]

        skt = None
        ce = '£' in decoded

        if len(parts3) > 1:
            date_part = parts3[1].split('£')[0]
            if date_part:
                skt = f"20{date_part[:2]}-{date_part[2:4]}-01"

        return {
            "stokKodu": stokKodu,
            "opsn": opsn,
            "lotNo": lotNo,
            "skt": skt,
            "ce": ce
        }

huffman_service = HuffmanService()

# @router.get("/merhaba")
async def merhaba_get():
    return {"mesaj": "Merhaba Dünya!"}


# @router.post("/encode")
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

# @router.post("/decode")
async def decode_barkod(request: DecodeRequest):
    try:
        result = await huffman_service.decode_barkod(request.barkod)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))