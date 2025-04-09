from db import get_connection

def test_oracle_connection():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT SYSDATE FROM dual")
        result = cursor.fetchone()
        print("Veritabanı bağlantısı başarılı! Şu anki tarih:", result[0])
        cursor.close()
        conn.close()
    except Exception as e:
        print("Bağlantı hatası:", e)

if __name__ == "__main__":
    test_oracle_connection()