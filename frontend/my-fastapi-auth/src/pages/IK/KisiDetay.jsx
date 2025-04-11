import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import api from "../../api/axios";

const KisiDetay = () => {
    const { id } = useParams();
    const [kisi, setKisi] = useState(null);
    const [loading, setLoading] = useState(true);

    const KisiDetay = ({ user }) => {
        return (
            <div>
                <h3>Kişi Detayı</h3>
                <p>Adı: {user.name}</p>
                <p>Email: {user.email}</p>
                <p>Telefon: {user.phone}</p>
                {/* Diğer kullanıcı bilgileri */}
            </div>
        );
    };

    useEffect(() => {
        const fetchKisi = async () => {
            try {
                const response = await api.get(`/ik/kisi-list`); // Tüm liste çekiliyor
                const selected = response.data.find((k) => k.ID === parseInt(id));
                setKisi(selected);
            } catch (error) {
                console.error("Detay verisi alınamadı:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchKisi();
    }, [id]);

    if (loading) return <p className="text-center mt-10">Yükleniyor...</p>;
    if (!kisi) return <p className="text-center mt-10">Kişi bulunamadı.</p>;

    return (
        <div className="p-6">
            <h2 className="text-2xl font-bold mb-4">Kişi Detay</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div><strong>Ad:</strong> {kisi.ADI}</div>
                <div><strong>Soyad:</strong> {kisi.SOYADI}</div>
                <div><strong>Kimlik No:</strong> {kisi.KIMLIK_NO}</div>
                <div><strong>Meslek:</strong> {kisi.MESLEGI}</div>
                <div><strong>Telefon:</strong> {kisi.CEP_TEL}</div>
                <div><strong>Adres:</strong> {kisi.ADRES}</div>
                <div><strong>Doğum Tarihi:</strong> {kisi.DOGUM_TARIHI?.split("T")[0]}</div>
                <div><strong>Birim No:</strong> {kisi.BIRIM_NO}</div>
                <div><strong>İşe Giriş:</strong> {kisi.ISE_GIRIS_TARIHI?.split("T")[0]}</div>
            </div>

            <div className="mt-6">
                <Link
                    to="/ik/kisi-list"
                    className="text-blue-500 hover:text-blue-700 underline"
                >
                    ← Geri Dön
                </Link>

                <Link
                    to={`/ik/kisi-duzenle/${kisi.ID}`}
                    className="text-green-600 hover:text-green-800 underline"
                >
                    ✏️ Düzenle
                </Link>

            </div>
        </div>
    );
};

export default KisiDetay;
