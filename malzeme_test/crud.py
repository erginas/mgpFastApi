from db import get_connection
from malzeme_test.models import Malzeme

def xget_all_malzeme():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MALZEME_NO, MALZEME_ADI FROM MALZEME where malzeme_no =22345")
    rows = cursor.fetchall()
    cols = [c[0].lower() for c in cursor.description]
    result = [Malzeme(**dict(zip(cols, row))) for row in rows]
    cursor.close()
    conn.close()
    return result