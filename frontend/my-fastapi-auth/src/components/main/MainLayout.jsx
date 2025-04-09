import React, { useState, useEffect } from "react";
import { LogOut, LayoutDashboard, PackageSearch, Settings } from "lucide-react";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@radix-ui/react-tabs";
import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";

const MainLayout = () => {
  const [activeTabs, setActiveTabs] = useState(["dashboard"]);
  const [selectedTab, setSelectedTab] = useState("dashboard");
  const [sidebarOpen, setSidebarOpen] = useState(true); // Sidebar açılma durumu
  const [currentDate, setCurrentDate] = useState("");
  const [userName, setUserName] = useState("");
  const [appVersion, setAppVersion] = useState("1.0.0");
  const [isMobile, setIsMobile] = useState(false); // Ekranın mobil olup olmadığını kontrol etmek için
  const navigate = useNavigate();

  // Modüllerin tanımlanması
  const modules = [
    { id: "dashboard", title: "Dashboard", icon: <LayoutDashboard size={18} /> },
    { id: "stok", title: "Stok", icon: <PackageSearch size={18} /> },
    { id: "ayarlar", title: "Ayarlar", icon: <Settings size={18} /> },
  ];

  useEffect(() => {
    const user = localStorage.getItem("userName"); // Kullanıcı adı kontrolü
    if (user) {
      setUserName(user);
    }

    const today = new Date();
    setCurrentDate(today.toLocaleDateString());

    // Ekran boyutuna göre sidebar'ın açılıp kapanmasını sağla
    const handleResize = () => {
      if (window.innerWidth < 1024) { // Eğer ekran 1024px'den küçükse mobil kabul et
        setIsMobile(true);
      } else {
        setIsMobile(false);
        setSidebarOpen(true); // Desktop ekranlarda sidebar açık kalsın
      }
    };

    window.addEventListener("resize", handleResize);
    handleResize(); // İlk renderda ekran boyutunu kontrol et

    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, []);

  const openTab = (id) => {
    if (!activeTabs.includes(id)) {
      setActiveTabs([...activeTabs, id]);
    }
    setSelectedTab(id);
  };

  const closeTab = (id) => {
    const filtered = activeTabs.filter((t) => t !== id);
    setActiveTabs(filtered);
    if (selectedTab === id && filtered.length > 0) {
      setSelectedTab(filtered[0]);
    }
  };

  const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("userName");
    navigate("/login");
  };

  // Sidebar'ı açma ve kapama fonksiyonu
  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  return (
    <div className="flex flex-col h-screen">
      {/* Top Bar */}
      <div className="bg-gray-800 text-white p-4 flex justify-between items-center">
        <h2 className="text-xl font-bold">Uygulama Adı</h2>
        <div className="flex items-center gap-4">
          <span>Hoşgeldiniz, {userName || "Bilinmeyen Kullanıcı"}</span>
          <button
            className="lg:hidden text-white"
            onClick={toggleSidebar} // Hamburger menüsünü tetikleyen buton
          >
            ☰ {/* Hamburger Menü */}
          </button>
        </div>
      </div>

      <div className="flex flex-1">
        {/* Sidebar */}
        <aside
          className={`lg:w-52 bg-gray-800 text-white p-4 flex flex-col gap-4 transition-all duration-300 ease-in-out ${
            sidebarOpen ? "w-52" : "w-0" // Sidebar gizlendiğinde genişlik 0 olmalı
          }`}
        >
          <h2 className={`text-xl font-bold mb-6 ${!sidebarOpen ? "hidden" : ""}`}>Modüller</h2>
          {modules.map((mod) => (
            <button
              key={mod.id}
              onClick={() => openTab(mod.id)}
              className="flex items-center gap-2 text-left hover:bg-gray-700 p-2 rounded"
            >
              {mod.icon}
              {sidebarOpen && mod.title}
            </button>
          ))}
          <div className="mt-auto">
            <button
              onClick={logout}
              className="flex items-center gap-2 bg-red-600 px-3 py-2 rounded hover:bg-red-700 w-full"
            >
              <LogOut size={18} /> Çıkış Yap
            </button>
          </div>
        </aside>

        {/* Main Area */}
        <div className="flex-1 flex flex-col bg-gray-50">
          <Tabs value={selectedTab} onValueChange={setSelectedTab} className="w-full">
            <TabsList className="flex bg-white border-b p-2 gap-2 overflow-x-auto">
              {activeTabs.map((tab) => (
                <div key={tab} className="flex items-center bg-gray-200 px-3 py-1 rounded-full">
                  <TabsTrigger value={tab} className="text-sm font-medium mr-2">
                    {modules.find((m) => m.id === tab)?.title || tab}
                  </TabsTrigger>
                  <button
                    onClick={() => closeTab(tab)}
                    className="text-gray-500 hover:text-red-500"
                  >
                    ✕
                  </button>
                </div>
              ))}
            </TabsList>

            {activeTabs.map((tab) => (
              <TabsContent key={tab} value={tab} className="p-4">
                <motion.div
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.3 }}
                >
                  <h1 className="text-xl font-bold mb-4">{modules.find((m) => m.id === tab)?.title}</h1>
                  <p>Buraya "{tab}" modülüne ait içerik gelecek.</p>
                </motion.div>
              </TabsContent>
            ))}
          </Tabs>
        </div>
      </div>

      {/* Bottom Info Bar */}
      <div className="bg-gray-800 text-white p-2 mt-auto flex justify-between items-center w-full">
        <div className="flex gap-4 text-sm">
          <span>Uygulama Versiyonu: {appVersion}</span>
          <span>Form Versiyonu: 1.0</span>
          <span>Kullanıcı: {userName || "Bilinmeyen Kullanıcı"}</span>
          <span>Tarih: {currentDate}</span>
        </div>
      </div>
    </div>
  );
};

export default MainLayout;
