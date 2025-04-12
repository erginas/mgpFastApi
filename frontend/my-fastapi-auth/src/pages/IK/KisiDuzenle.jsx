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

/*    const handleChange = (e) => {
        const { name, value } = e.target;
        setKisi((prev) => ({
            ...prev,
            [name]: value,
        }));
    };*/

/*    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await api.put(`/ik/kisi/${id}`, kisi); // endpoint örnek, backend'e göre değişebilir
            navigate(`/ik/kisi-detay/${id}`);
        } catch (error) {
            console.error("Güncelleme hatası:", error);
        }
    };*/

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = () => {
        console.log("Güncellenen Veri:", formData);
        // Burada API çağrısı yapılabilir
        onSave();
    };

    if (loading) return <p>Yükleniyor...</p>;
    if (!kisi) return <p>Kişi bulunamadı.</p>;

    return (
        <div>
            <h2 className="text-xl font-bold mb-4">{user.ADI} {user.SOYADI} Düzenle</h2>
            <form onSubmit={(e) => e.preventDefault()} className="space-y-4">
                <div>
                    <label className="block mb-1">Ad</label>
                    <input
                        type="text"
                        name="ADI"
                        value={formData.ADI}
                        onChange={handleChange}
                        className="p-2 border rounded w-full"
                    />
                </div>
                <div>
                    <label className="block mb-1">Soyad</label>
                    <input
                        type="text"
                        name="SOYADI"
                        value={formData.SOYADI}
                        onChange={handleChange}
                        className="p-2 border rounded w-full"
                    />
                </div>
                <div>
                    <label className="block mb-1">Kimlik No</label>
                    <input
                        type="text"
                        name="KIMLIK_NO"
                        value={formData.KIMLIK_NO}
                        onChange={handleChange}
                        className="p-2 border rounded w-full"
                    />
                </div>
                <div>
                    <label className="block mb-1">Birim No</label>
                    <input
                        type="text"
                        name="BIRIM_NO"
                        value={formData.BIRIM_NO}
                        onChange={handleChange}
                        className="p-2 border rounded w-full"
                    />
                </div>
                <button
                    type="submit"
                    onClick={handleSubmit}
                    className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600 transition-colors"
                >
                    Kaydet
                </button>
            </form>
        </div>
    );
};
export default KisiDuzenle;
