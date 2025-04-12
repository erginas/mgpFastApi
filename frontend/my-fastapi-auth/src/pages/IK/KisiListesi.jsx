import React, { useEffect, useState } from "react";
import api from "../../api/axios";
import { DataGrid } from "@mui/x-data-grid";

const KisiListesi = ({ onSelectUser }) => {
    const [kisiler, setKisiler] = useState([]);
    const [filtered, setFiltered] = useState([]);
    const [loading, setLoading] = useState(true);

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
                if (!response.data || response.data.length === 0) {
                    console.error("API'den gelen veri boş.");
                    return;
                }
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

    // Çift tıklama işlevi
    const handleRowDoubleClick = (params) => {
        if (!params.row) {
            console.error("Seçilen kişi bilgisi bulunamadı.");
            return;
        }
        console.log("Seçilen Kişi:", params.row); // Seçilen kişiyi kontrol et
        onSelectUser(params.row, "detay"); // Detay tabı aç
    };

    // Sağ tıklama işlevi
    const [contextMenu, setContextMenu] = useState(null);

    const handleContextMenu = (event, params) => {
        event.preventDefault();
        if (!params.row) {
            console.error("Seçilen kişi bilgisi bulunamadı.");
            return;
        }
        console.log("Sağ Tıklanan Kişi:", params.row); // Sağ tıklanan kişiyi kontrol et
        setContextMenu(
            contextMenu === null
                ? {
                    mouseX: event.clientX + 2,
                    mouseY: event.clientY - 6,
                    rowData: params.row
                }
                : null
        );
    };

    const handleEditClick = () => {
        if (!contextMenu?.rowData) {
            console.error("Seçilen kişi bilgisi bulunamadı.");
            return;
        }
        console.log("Düzenlenecek Kişi:", contextMenu.rowData); // Düzenlenecek kişiyi kontrol et
        onSelectUser(contextMenu.rowData, "duzenle"); // Düzenleme tabı aç
        setContextMenu(null);
    };

    if (loading) return <p className="text-center mt-10">Yükleniyor...</p>;

    // DataGrid için sütun tanımları
    const columns = [
        { field: "id", headerName: "ID", width: 80 },
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
                    onChange={(e) => setFilter({ ...filter, ad: e.target.value })}
                    className="p-2 border rounded"
                />
                <input
                    type="text"
                    name="soyad"
                    placeholder="Soyad"
                    value={filter.soyad}
                    onChange={(e) => setFilter({ ...filter, soyad: e.target.value })}
                    className="p-2 border rounded"
                />
                <input
                    type="text"
                    name="kimlik_no"
                    placeholder="Kimlik No"
                    value={filter.kimlik_no}
                    onChange={(e) => setFilter({ ...filter, kimlik_no: e.target.value })}
                    className="p-2 border rounded"
                />
                <input
                    type="text"
                    name="birim_no"
                    placeholder="Birim No"
                    value={filter.birim_no}
                    onChange={(e) => setFilter({ ...filter, birim_no: e.target.value })}
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
                    onRowDoubleClick={handleRowDoubleClick}
                    onRowContextMenu={(event, params) => handleContextMenu(event, params)}
                    disableSelectionOnClick
                    loading={loading}
                    localeText={{
                        noRowsLabel: "Kayıt bulunamadı."
                    }}
                />
            </div>

            {/* Sağ Tıklama Menüsü */}
            {contextMenu && (
                <div
                    style={{
                        position: "absolute",
                        top: contextMenu.mouseY,
                        left: contextMenu.mouseX,
                        backgroundColor: "#fff",
                        boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)",
                        padding: "8px",
                        borderRadius: "4px",
                        zIndex: 1000
                    }}
                >
                    <button
                        onClick={handleEditClick}
                        style={{ display: "block", width: "100%", padding: "8px", textAlign: "left" }}
                    >
                        Düzenle
                    </button>
                </div>
            )}
        </div>
    );
};

export default KisiListesi;