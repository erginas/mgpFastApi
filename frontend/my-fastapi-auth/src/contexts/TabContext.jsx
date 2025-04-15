import React, { createContext, useState, useContext } from "react";

// TabContext
const TabContext = createContext();

export const TabProvider = ({ children }) => {
    const [mainTabs, setMainTabs] = useState([]); // Sekme listesini tutuyor
    const [selectedTab, setSelectedTab] = useState(null); // Seçili sekmeyi tutuyor

    // Tab ekleme fonksiyonu
    const openTab = (id, title) => {
        // Eğer bu sekme zaten yoksa, listeye ekle
        if (!mainTabs.find((tab) => tab.id === id)) {
            setMainTabs((prevTabs) => [
                ...prevTabs,
                { id, title },
            ]);
        }
        setSelectedTab(id); // Tab açıldığında aktif tab'ı ayarla
    };

    // Tab kapama fonksiyonu
    const closeTab = (id) => {
        setMainTabs((prevTabs) => prevTabs.filter((tab) => tab.id !== id));
    };

    return (
        <TabContext.Provider
            value={{
                mainTabs,
                selectedTab,
                setSelectedTab,
                openTab,
                closeTab,
            }}
        >
            {children}
        </TabContext.Provider>
    );
};

// Custom hook ile context'e erişim
export const useTabContext = () => useContext(TabContext);
