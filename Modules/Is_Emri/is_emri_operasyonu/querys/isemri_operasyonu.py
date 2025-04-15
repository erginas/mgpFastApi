query = """
        SELECT 
            io.OPERASYON_NO, 
            CASE 
                WHEN io.durumu = 'S' THEN 'Sonlanmş' 
                WHEN io.durumu = 'D' THEN 'Durmuş' 
                WHEN io.durumu = 'I' THEN 'İşler' 
                ELSE 'Diğer' 
            END Durumu,
            io.ISLEM_BASLANGIC, 
            io.ISLEM_BITIS, 
            io.miktar_giren,
            io.miktar_cikan, 
            k.adi || ' ' || k.soyadi AS adi_soyadi,
            ie.ACIKLAMA, 
            ie.CE_FL, 
            ie.DURUMU AS isemri_durum, 
            ie.EK_BILGI, 
            ie.ONCELIK, 
            ie.RECETE_ID, 
            ie.RECETE_NO, 
            ie.REF_BELGE_NO,
            m.stok_kodu, 
            m.opsn, 
            m.malzeme_adi
        FROM IS_EMRI_OPERASYONU io
        LEFT OUTER JOIN kisi k ON k.kimlik_no = io.KIMLIK_NO
        LEFT OUTER JOIN is_emri ie ON io.ISEMRI_NO = ie.ISEMRI_NO
        LEFT OUTER JOIN OPERASYON o ON o.OPERASYON_NO = io.OPERASYON_NO
        LEFT OUTER JOIN malzeme m ON m.MALZEME_NO = ie.MALZEME_NO
        WHERE io.isemri_no = :isemri_no
    """