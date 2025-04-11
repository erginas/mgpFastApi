import React, { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import api from "../../api/axios";

const KisiDuzenle = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [kisi, setKisi] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchKisi = async () => {
            try {
                const response = await api.get("/ik/kisi-list");
                const found = response.data.find((item) => item.ID === parseInt(id));
                setKisi(found);
            } catch (error) {
                console.error("Kişi getirilemedi:", error);
            } finally {
                setLoading(false);
            }
        };
        fetchKisi();
    }, [id]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setKisi((prev) => ({
            ...prev,
            [name]: value,
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await api.put(`/ik/kisi/${id}`, kisi); // endpoint örnek, backend'e göre değişebilir
            navigate(`/ik/kisi-detay/${id}`);
        } catch (error) {
            console.error("Güncelleme hatası:", error);
        }
    };

    if (loading) return <p>Yükleniyor...</p>;
    if (!kisi) return <p>Kişi bulunamadı.</p>;

    return (
        <div className="p-6">
            <h2 className="text-2xl font-bold mb-4">Kişi Düzenle</h2>
            <form onSubmit={handleSubmit} className="space-y-4 max-w-xl">
                <div>
                    <label className="block">Adı</label>
                    <input
                        type="text"
                        name="ADI"
                        value={kisi.ADI || ""}
                        onChange={handleChange}
                        className="w-full border p-2 rounded"
                    />
                </div>
                <div>
                    <label className="block">Soyadı</label>
                    <input
                        type="text"
                        name="SOYADI"
                        value={kisi.SOYADI || ""}
                        onChange={handleChange}
                        className="w-full border p-2 rounded"
                    />
                </div>
                <div>
                    <label className="block">Mesleği</label>
                    <input
                        type="text"
                        name="MESLEGI"
                        value={kisi.MESLEGI || ""}
                        onChange={handleChange}
                        className="w-full border p-2 rounded"
                    />
                </div>
                <div>
                    <label className="block">Cep Tel</label>
                    <input
                        type="text"
                        name="CEP_TEL"
                        value={kisi.CEP_TEL || ""}
                        onChange={handleChange}
                        className="w-full border p-2 rounded"
                    />
                </div>
                {/* İstersen daha fazla alan ekleyebiliriz */}

                <button
                    type="submit"
                    className="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
                >
                    Kaydet
                </button>
            </form>
        </div>
    );
};

export default KisiDuzenle;
