from core.huffman2_service import decode_barkod, eng_decode,encode_barkod
# from core.huffman_service import decodeBarkod

# Örnek veri
data = "6575345535666016524115622606161291"

# # Huffman kodlaması uygula
# encoded_data = eng_encode(data)
# print(f"Orijinal Veri: {data}")
# print(f"Kodlanmış Veri: {encoded_data}")

# Huffman kodunu çöz

decoded_data = eng_decode(data)
print(f"Çözülmüş Veri: {decoded_data}")

# Doğrulama
assert data == decoded_data, "Kodlama ve çözme işlemleri eşleşmiyor!"
print("Test başarılı: Kodlama ve çözme işlemleri doğru çalışıyor.")