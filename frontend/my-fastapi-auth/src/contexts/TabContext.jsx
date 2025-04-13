import React, { createContext, useContext, useState } from "react";

const TabContext = createContext();

export const TabProvider = ({ children }) => {
    const [mainTabs, setMainTabs] = useState([
        { id: "dashboard", title: "Dashboard", component: "Dashboard" }
    ]);
    const [activeMainTab, setActiveMainTab] = useState("dashboard");

    const [altTabs, setAltTabs] = useState({});
    const [activeAltTab, setActiveAltTab] = useState({});

    // Ana sekme ekle
    const addMainTab = (tab) => {
        setMainTabs((prev) => {
            if (!prev.find((t) => t.id === tab.id)) return [...prev, tab];
            return prev;
        });
        setActiveMainTab(tab.id);
    };

    // Alt sekme ekle
    const addAltTab = (moduleId, tab) => {
        setAltTabs((prev) => {
            const moduleTabs = prev[moduleId] || [];
            const exists = moduleTabs.find((t) => t.id === tab.id);
            if (exists) return prev;
            return {
                ...prev,
                [moduleId]: [...moduleTabs, tab]
            };
        });
        setActiveAltTab((prev) => ({ ...prev, [moduleId]: tab.id }));
    };

    const removeMainTab = (tabId) => {
        setMainTabs((prev) => prev.filter((t) => t.id !== tabId));
    };

    const removeAltTab = (moduleId, tabId) => {
        setAltTabs((prev) => {
            const filtered = (prev[moduleId] || []).filter((t) => t.id !== tabId);
            return { ...prev, [moduleId]: filtered };
        });
    };

    return (
        <TabContext.Provider
            value={{
                mainTabs,
                activeMainTab,
                setActiveMainTab,
                addMainTab,
                removeMainTab,

                altTabs,
                activeAltTab,
                setActiveAltTab,
                addAltTab,
                removeAltTab
            }}
        >
            {children}
        </TabContext.Provider>
    );
};

export const useTabContext = () => useContext(TabContext);
