import React from "react";
import { useTabContext } from "@/contexts/TabContext";

const AltTabs = () => {
    const { mainTabs, selectedTab, closeTab } = useTabContext();

    return (
        <div className="w-full">
            <div className="flex gap-2 p-2 border-b bg-white">
                {mainTabs.map((tab) => (
                    <div
                        key={tab.id}
                        className={`text-sm font-medium py-2 px-4 rounded-md cursor-pointer ${
                            selectedTab === tab.id ? "bg-sky-500 text-white" : "bg-gray-100 text-gray-600"
                        }`}
                        onClick={() => {
                            // Aktif tabı seçmek
                        }}
                    >
                        {tab.title}
                        <span
                            onClick={() => closeTab(tab.id)}
                            className="ml-2 text-xs text-gray-500 cursor-pointer"
                        >
                            X
                        </span>
                    </div>
                ))}
            </div>

            <div className="p-4 bg-white">
                {selectedTab ? (
                    <div>
                        {/* Tab içeriği burada render edilecek */}
                    </div>
                ) : (
                    <p>Alt Sekme İçeriği Bulunamadı.</p>
                )}
            </div>
        </div>
    );
};

export default AltTabs;
