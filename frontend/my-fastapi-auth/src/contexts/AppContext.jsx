import { createContext, useContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import api from "@/api/axios";

const AppContext = createContext();

export function AppProvider({ children }) {
    const navigate = useNavigate();

    // 👇 Tüm state'ler burada
    const [sidebarOpen, setSidebarOpen] = useState(true);
    const [isMobile, setIsMobile] = useState(false);
    const [currentDate, setCurrentDate] = useState("");
    const [userInfo, setUserInfo] = useState({ full_name: "", profile_path: "", title: "" });
    const [selectedUser, setSelectedUser] = useState(null);

    // Tab Management
    const [activeTabs, setActiveTabs] = useState(["dashboard"]);
    const [selectedTab, setSelectedTab] = useState("dashboard");
    const [altTabs, setAltTabs] = useState({});
    const [activeAltTab, setActiveAltTab] = useState(null);
    const [moduleComponents, setModuleComponents] = useState({ dashboard: <Dashboard /> });

    // Modüller
    const modules = [
        { id: "dashboard", title: "Dashboard", icon: <LayoutDashboard size={18} /> },
        { id: "stok", title: "Stok", icon: <PackageSearch size={18} /> },
        { id: "kisiler", title: "Kişiler", icon: <User size={18} /> },
    ];

    // 👇 Fonksiyonlar
    const toggleSidebar = () => setSidebarOpen(!sidebarOpen);

    const openTab = (id, title, component) => {
        if (!activeTabs.includes(id)) {
            setActiveTabs(prev => [...prev, id]);
            setModuleComponents(prev => ({ ...prev, [id]: component }));
        }
        setSelectedTab(id);
    };

    const handleAltTabAdd = (moduleKey, user) => {
        setAltTabs(prev => {
            const newTab = {
                key: `detay-${user.id}`,
                label: `${user.ADI} Detay`,
                component: <KisiDetay user={user} />
            };
            const moduleTabs = prev[moduleKey] || [];
            return moduleTabs.some(tab => tab.key === newTab.key)
                ? prev
                : { ...prev, [moduleKey]: [...moduleTabs, newTab] };
        });
    };

    // Diğer fonksiyonlar (logout, handleUserSubmit vb.) buraya...

    return (
        <AppContext.Provider
            value={{
                // State'ler
                sidebarOpen, isMobile, currentDate, userInfo, selectedUser,
                activeTabs, selectedTab, altTabs, activeAltTab, moduleComponents, modules,

                // Fonksiyonlar
                toggleSidebar, openTab, handleAltTabAdd,
                setSelectedTab, setAltTabs, setActiveAltTab
            }}
        >
            {children}
        </AppContext.Provider>
    );
}

export const useApp = () => useContext(AppContext);