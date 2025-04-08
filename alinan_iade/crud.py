from alinan_iade.models import Aktarma
from db import get_connection


def get_all_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT 
        stok_kodu,
        malzeme_no
    FROM AKTARMA
        """)
    rows = cursor.fetchall()
    cols = [c[0].lower() for c in cursor.description]
    result = [Aktarma(**dict(zip(cols, row))) for row in rows]
    cursor.close()
    conn.close()
    return result

def insert_data(data: Aktarma):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO AKTARMA (stok_kodu, malzeme_no) VALUES (:1, :2)
    """, (data.stok_kodu, data.malzeme_no))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Kayıt eklendi."}

def update_data(malzeme_no: int, data: Aktarma):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE AKTARMA SET stok_kodu = :1 WHERE malzeme_no = :2
    """, (data.stok_kodu, malzeme_no))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Kayıt güncellendi."}

def delete_data(malzeme_no: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM AKTARMA WHERE malzeme_no = :1
    """, (malzeme_no,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Kayıt silindi."}