import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../../api/axios";
import { DataGrid } from "@mui/x-data-grid";

const KisiListesi = () => {
    const [kisiler, setKisiler] = useState([]);
    const [filtered, setFiltered] = useState([]);
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    // Filtre alanları
    const [filter, setFilter] = useState({
        ad: "",
        soyad: "",
        kimlik_no: "",
        birim_no: ""
    });

    // Veriyi API'den çekme
    useEffect(() => {
        const fetchKisiler = async () => {
            try {
                const response = await api.get("/ik/kisi-list");
                setKisiler(response.data);
                setFiltered(response.data); // Başlangıçta tüm veriyi göster
            } catch (error) {
                console.error("Veri alınamadı:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchKisiler();
    }, []);

    // Filtreleme mantığı
    useEffect(() => {
        const filteredData = kisiler.filter((kisi) =>
            (filter.ad === "" || kisi.ADI?.toLowerCase().includes(filter.ad.toLowerCase())) &&
            (filter.soyad === "" || kisi.SOYADI?.toLowerCase().includes(filter.soyad.toLowerCase())) &&
            (filter.kimlik_no === "" || String(kisi.KIMLIK_NO).includes(filter.kimlik_no)) &&
            (filter.birim_no === "" || String(kisi.BIRIM_NO) === filter.birim_no)
        );
        setFiltered(filteredData);
    }, [filter, kisiler]);

    // Filtre inputlarını dinleme
    const handleChange = (e) => {
        setFilter({ ...filter, [e.target.name]: e.target.value });
    };

    // Satır tıklama işlevi
    const handleRowClick = (params) => {
        navigate(`/ik/kisi-detay/${params.row.id}`);
    };

    if (loading) return <p className="text-center mt-10">Yükleniyor...</p>;

    // DataGrid için sütun tanımları
    const columns = [
        { field: "ADI", headerName: "Ad", width: 150 },
        { field: "SOYADI", headerName: "Soyad", width: 150 },
        { field: "KIMLIK_NO", headerName: "Kimlik No", width: 150 },
        { field: "BIRIM_NO", headerName: "Birim No", width: 150 }
    ];

    // DataGrid için satırlar
    const rows = filtered.map((kisi, index) => ({
        id: kisi.id || index + 1,
        ADI: kisi.ADI,
        SOYADI: kisi.SOYADI,
        KIMLIK_NO: kisi.KIMLIK_NO,
        BIRIM_NO: kisi.BIRIM_NO
    }));

    return (
        <div>
            {/* Filtreleme Formu */}
            <div className="mb-4 flex gap-2">
                <input
                    type="text"
                    name="ad"
                    placeholder="Ad"
                    value={filter.ad}
                    onChange={handleChange}
                    className="p-2 border rounded"
                />
                <input
                    type="text"
                    name="soyad"
                    placeholder="Soyad"
                    value={filter.soyad}
                    onChange={handleChange}
                    className="p-2 border rounded"
                />
                <input
                    type="text"
                    name="kimlik_no"
                    placeholder="Kimlik No"
                    value={filter.kimlik_no}
                    onChange={handleChange}
                    className="p-2 border rounded"
                />
                <input
                    type="text"
                    name="birim_no"
                    placeholder="Birim No"
                    value={filter.birim_no}
                    onChange={handleChange}
                    className="p-2 border rounded"
                />
            </div>

            {/* Material-UI DataGrid Tablosu */}
            <div style={{ height: 400, width: "100%" }}>
                <DataGrid
                    rows={rows}
                    columns={columns}
                    pageSize={5}
                    rowsPerPageOptions={[5, 10, 20]}
                    onRowClick={handleRowClick}
                    disableSelectionOnClick
                    loading={loading}
                    localeText={{
                        noRowsLabel: "Kayıt bulunamadı."
                    }}
                />
            </div>
        </div>
    );
};

export default KisiListesi;