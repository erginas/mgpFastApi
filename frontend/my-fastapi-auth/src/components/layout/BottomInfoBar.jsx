// BottomInfoBar.jsx
import React from "react";

const BottomInfoBar = ({ currentDate, userName }) => {
    return (
        <div className="bg-sky-600 text-sky-100 p-3 flex justify-end w-full">
            <div className="flex flex-wrap justify-end gap-5 text-sm">
                <span>Uygulama Versiyonu: 2.0</span>
                <span>Form Versiyonu: 1.0</span>
                <span>Kullanıcı: {userName || "Bilinmeyen Kullanıcı"}</span>
                <span>Tarih: {currentDate}</span>
                <span className="font-medium text-cyan-200">e-Tıpsan Web | ⒸTıpsan</span>
            </div>
        </div>
    );
};

export default BottomInfoBar;