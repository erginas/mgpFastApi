from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date
import pendulum

# from huffman_data import huffman
# Huffman kodlama tablosu
huffman = [
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



app = FastAPI()

class EncodeBarkodRequest(BaseModel):
    stokKodu: str
    opsn: str
    lotNo: str
    skt: date = None
    ce: bool = False

class DecodeBarkodRequest(BaseModel):
    barkod: str

@app.post("/encode-barkod")
async def encode_barkod(request: EncodeBarkodRequest):
    """
    Barkod oluşturmak için kullanılan endpoint.
    """
    try:
        # HuffmanService sınıfındaki encodeBarkod metodunu çağır
        encoded_barkod = await encodeBarkod(
            request.stokKodu,
            request.opsn,
            request.lotNo,
            request.skt,
            request.ce
        )
        return {"encoded_barkod": encoded_barkod}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Beklenmeyen hata: {str(e)}")

@app.post("/decode-barkod")
async def decode_barkod(request: DecodeBarkodRequest):
    """
    Barkod çözmek için kullanılan endpoint.
    """
    try:
        # HuffmanService sınıfındaki decodeBarkod metodunu çağır
        decoded_data = await decodeBarkod(request.barkod)
        return decoded_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Beklenmeyen hata: {str(e)}")

# HuffmanService metotlarını burada tanımlayalım
async def encode(data: str) -> str:
    result = ""
    for char in data:
        item = next((x for x in huffman if x["key"] == f"+{char}+"), None)
        if item:
            result += item["value"]
    return result

async def huffmanSifrele(xs: str) -> str:
    huffmanMap = {item["key"]: item["value"] for item in huffman}
    txt = ""

    for char in xs:
        kod = f"+{char}+"
        value = huffmanMap.get(kod)
        if not value:
            return ""
        txt += value

    deger = ""
    while txt:
        str_chunk = txt[:3]
        if len(str_chunk) == 3:
            deger += str(int(str_chunk, 2))
        elif len(str_chunk) == 2:
            deger += f"8{int(str_chunk, 2)}"
        elif len(str_chunk) == 1:
            deger += f"9{int(str_chunk, 2)}"
        txt = txt[3:]

    uz = len(deger)
    tamDeger = uz // 2
    yariDeger = uz / 2

    if tamDeger != yariDeger:
        deger += "9"

    return deger

async def huffmanSifreCoz(xs: str) -> str:
    txt = ""
    dd = ""
    nineKontrol = xs[-1]
    if nineKontrol == "9":
        xs = xs[:-1]

    for i in range(len(xs)):
        if not ("0" <= xs[i] <= "9"):
            return ""

    for i in range(len(xs)):
        dgr = int(xs[i])
        if dgr < 8:
            txt += format(dgr, "03b")
        else:
            kontrol = xs[i + 1]
            if not kontrol:
                return ""
            txt += format(int(kontrol), "02b") if dgr == 8 else format(int(kontrol), "01b")
            break

    huffmanMap = {item["value"]: item["key"] for item in huffman}

    while txt:
        found = False
        for key, value in huffmanMap.items():
            if txt.startswith(key):
                dd += value[1:-1]
                txt = txt[len(key):]
                found = True
                break
        if not found:
            if txt != "0":
                return ""
            break

    return dd

async def encodeBarkod(stokKodu: str, opsn: str, lotNo: str, skt: date, ce: bool) -> str:
    # skt_str = f"${dayjs(skt).format('YYMM')}" if skt else ""
    skt_str = f"${pendulum.instance(skt).format('YYMM')}" if skt else ""
    ce_str = "£" if ce else ""
    return await huffmanSifrele(f"{stokKodu}@{opsn}~{lotNo}{skt_str}{ce_str}")

async def decodeBarkod(barkod: str):
    decoded = await huffmanSifreCoz(barkod)
    parts = decoded.split("@")
    stokKodu = parts[0]
    parts2 = parts[1].split("~")
    opsn = parts2[0]
    parts3 = parts2[1].split("$")
    lotNo = parts3[0]
    part4 = parts3[1].split("£") if len(parts3) > 1 else ["", ""]
    skt = f"20{part4[0][:2]}-{part4[0][2:4]}-01" if part4[0] else None
    ce = "£" in decoded
    return {"stokKodu": stokKodu, "opsn": opsn, "lotNo": lotNo, "skt": skt, "ce": ce}


# Huffman kodlama fonksiyonu
def eng_encode(data: str) -> str:
    result = ""
    for char in data:
        item = next((x for x in huffman if x["key"] == f"+{char}+"), None)
        if item:
            result += item["value"]
    return result

# Huffman çözme fonksiyonu
def eng_decode(encoded_data: str) -> str:
    huffman_map = {item["value"]: item["key"] for item in huffman}
    decoded = ""
    temp = ""

    for bit in encoded_data:
        temp += bit
        if temp in huffman_map:
            decoded += huffman_map[temp][1]  # '+0+' -> '0'
            temp = ""

    return decoded