import React, { useState, useEffect } from "react";
import { LogOut, LayoutDashboard, PackageSearch, Settings, ChevronLeft, ChevronRight, User } from "lucide-react";
import {
    Tabs,
    TabsList,
    TabsTrigger,
    TabsContent
} from "@/components/ui/tabs";
import { useNavigate } from "react-router-dom";

import GenericFormModal from "../forms/GenericFormModal.jsx";
import Dashboard from "../dashboard/Dashboard.jsx";
import api from "@/api/axios.js";
import KisiListesi from "@/pages/IK/KisiListesi.jsx";
import KisiDetay from "@/pages/IK/KisiDetay.jsx";
import KisiDuzenle from "@/pages/IK/KisiDuzenle.jsx";
import TopBar from "@/components/layout/TopBar.jsx";
import Sidebar from "@/components/layout/SideBar.jsx";
import ContentArea from "@/components/layout/ContentArea.jsx";
import BottomInfoBar from "@/components/layout/BottomInfoBar.jsx";
import UserModal from "@/components/layout/UserModal.jsx"; // Düzenleme bileşeni

const MainLayout = () => {
    const [activeTabs, setActiveTabs] = useState(["dashboard"]);
    const [selectedTab, setSelectedTab] = useState("dashboard");
    const [sidebarOpen, setSidebarOpen] = useState(true);
    const [currentDate, setCurrentDate] = useState("");
    const [isMobile, setIsMobile] = useState(false);
    const [activeAltTab, setActiveAltTab] = useState(null);

    const [userInfo, setUserInfo] = useState({
        full_name: "",
        profile_path: "",
        title: ""
    });

    const [selectedUser, setSelectedUser] = useState(null);
    const [isUserModalOpen, setIsUserModalOpen] = useState(false);
    const [userName, setUserName] = useState("");
    const [profilePath, setProfilePath] = useState("");
    const [title, setTitle] = useState("");
    const navigate = useNavigate();
    const [altTabs, setAltTabs] = useState({});


    const modules = [
        { id: "dashboard", title: "Dashboard", icon: <LayoutDashboard size={18} /> },
        { id: "stok", title: "Stok", icon: <PackageSearch size={18} /> },
        { id: "ayarlar", title: "Ayarlar", icon: <Settings size={18} /> },
        { id: "kisiler", title: "Kişiler", icon: <User size={18} /> },
    ];


    // Alt tab ekleme
    const handleAltTabAdd = (moduleKey, user) => {
        console.log("Alt sekme ekleniyor:", moduleKey, user); // Bunu ekle

        setAltTabs((prev) => {
            const newTab = {
                key: `detay-${user.id}`,
                label: `${user.ADI} Detay`,
                component: <KisiDetay user={user} />,
            };

            const moduleTabs = prev[moduleKey] || [];
            const exists = moduleTabs.some((tab) => tab.key === newTab.key);

            if (exists) return prev;

            return {
                ...prev,
                [moduleKey]: [...moduleTabs, newTab],
            };
        });
    };

    // 👤 Kişi seçimi
    const handleUserSelect = (user, action = "detay") => {
        if (!user) return;

        if (selectedTab !== "kisiler") {
            setSelectedTab("kisiler"); // kisiler sekmesine geç
        }

        // Alt sekme ekle (ama ana tab açma!)
        handleAltTabAdd("kisiler", user);
    };



    const [moduleComponents, setModuleComponents] = useState({
        dashboard: <Dashboard />,
        // kisiler: <KisiListesi onSelectUser={handleUserSelect} />,
    });


    // Yeni bir tab açma
    const openTab = (id, title, component) => {
        if (!activeTabs.includes(id)) {
            setActiveTabs((prevTabs) => [...prevTabs, id]);
            setModuleComponents((prev) => ({
                ...prev,
                [id]: component,
            }));
        }
        setSelectedTab(id);
    };

    // ❌ Tab kapama
    const closeTab = (id) => {
        const filtered = activeTabs.filter((t) => t !== id);
        setActiveTabs(filtered);
        setModuleComponents((prev) => {
            const updated = { ...prev };
            delete updated[id];
            return updated;
        });
        if (selectedTab === id && filtered.length > 0) {
            setSelectedTab(filtered[0]);
        }
    };



    // Çıkış yapma
    const logout = () => {
        localStorage.removeItem("token");
        localStorage.removeItem("userName");
        navigate("/login");
    };

    // Yanıtlarla sidebar görünümü değiştirme
    const toggleSidebar = () => {
        setSidebarOpen(!sidebarOpen);
    };

    // Kullanıcı bilgilerini düzenleme
    const handleEdit = (userInfo) => {
        console.log("Editing user:", userInfo);
        setSelectedUser(userInfo);
        setIsUserModalOpen(true);
    };

    useEffect(() => {
        const getUserProfile = async () => {
            const token = localStorage.getItem("token");
            if (!token) {
                navigate("/login");
                return;
            }

            try {
                const response = await api.get("/profile");
                setUserInfo({
                    full_name: response.data.full_name,
                    profile_path: response.data.profile_path,
                    title: response.data.title
                });
            } catch (error) {
                console.error("Kullanıcı bilgileri alınırken hata oluştu:", error.response?.data || error.message);
                if (error.response?.status === 401) {
                    navigate("/login");
                }
            }
        };

        const user = localStorage.getItem("userName");
        if (user) {
            setUserName(user);
        }

        const today = new Date();
        setCurrentDate(today.toLocaleDateString());

        console.log("Selected User:", selectedUser);
        if (selectedUser) {
            setFormData({ ...selectedUser });
        }

        const handleResize = () => {
            const isMobileView = window.innerWidth < 1024;
            setIsMobile(isMobileView);
            setSidebarOpen(!isMobileView);
        };

        window.addEventListener("resize", handleResize);
        handleResize();

        getUserProfile();

        return () => {
            window.removeEventListener("resize", handleResize);
        };
    }, [navigate]);

    moduleComponents.kisiler = <KisiListesi onSelectUser={handleUserSelect} />;

    const handleUserSubmit = async (formData) => {
        console.log("API'ye Gönderilen Veriler:", formData);
        try {
            const response = await api.put("/profile", formData);
            console.log("API'den Gelen Yanıt:", response.data);
            setUserInfo(response.data);
            setUserName(response.data.full_name);
            setProfilePath(response.data.profile_path);
            setTitle(response.data.title);
            setIsUserModalOpen(false);
        } catch (error) {
            console.error("Kullanıcı bilgileri güncellenirken hata oluştu:", error.response?.data || error.message);
        }
    };

    const toggleUserModal = () => {
        handleEdit(userInfo);
        setIsUserModalOpen(!isUserModalOpen);
    };

    useEffect(() => {
        const tabs = altTabs["kisiler"];
        if (tabs && tabs.length > 0) {
            setActiveAltTab(tabs[tabs.length - 1].key); // en son eklenen aktif olsun
        }
    }, [altTabs]);


    console.log("altTabs[kisiler]:", altTabs["kisiler"]);

    return (
        <div className="main-layout flex flex-col h-screen bg-sky-50">
            {/* Top Bar */}
            <TopBar
                sidebarOpen={sidebarOpen}
                toggleSidebar={toggleSidebar}
                userName={userName}
                toggleUserModal={toggleUserModal}
            />

            {/* Main Content Area */}
            <div className="flex flex-1 overflow-hidden">
                {/* Sidebar */}
                <Sidebar
                    modules={modules}
                    sidebarOpen={sidebarOpen}
                    selectedTab={selectedTab}
                    openTab={openTab}
                />

                {/* Content Area */}
                <ContentArea
                    activeTabs={activeTabs}
                    selectedTab={selectedTab}
                    setSelectedTab={setSelectedTab}
                    closeTab={closeTab}
                    moduleComponents={moduleComponents}
                    altTabs={altTabs}
                    activeAltTab={activeAltTab}
                    setActiveAltTab={setActiveAltTab}
                />
            </div>

            {/* Bottom Info Bar */}
            <BottomInfoBar currentDate={currentDate} userName={userName} />

            {/* Kullanıcı düzenleme modalı */}
            <UserModal
                isOpen={isUserModalOpen}
                onClose={() => setIsUserModalOpen(false)}
                onSubmit={handleUserSubmit}
                initialData={selectedUser}
            />
        </div>
    );
};

export default MainLayout;