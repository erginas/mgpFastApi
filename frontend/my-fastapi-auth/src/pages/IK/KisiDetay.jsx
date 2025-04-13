// src/pages/IK/KisiDetay.jsx

import React from "react";

const KisiDetay = ({ user }) => {
    return (
        <div className="p-4 border rounded shadow">
            <h2 className="text-xl font-bold mb-2">Kişi Detayı</h2>
            <p><strong>Ad:</strong> {user.ADI}</p>
            <p><strong>Soyad:</strong> {user.SOYADI}</p>
            <p><strong>Kimlik No:</strong> {user.KIMLIK_NO}</p>
            <p><strong>Birim No:</strong> {user.BIRIM_NO}</p>
        </div>
    );
};

export default KisiDetay;
