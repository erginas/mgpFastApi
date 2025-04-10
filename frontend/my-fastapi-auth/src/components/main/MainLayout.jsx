import React, { useState ,useEffect } from "react";
import { LogOut, LayoutDashboard, PackageSearch, Settings, ChevronLeft, ChevronRight, User } from "lucide-react";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@radix-ui/react-tabs";
import { motion } from "framer-motion";
import { useNavigate } from "react-router-dom";

import GenericFormModal from "../forms/GenericFormModal.jsx";
import Dashboard from "../dashboard/Dashboard.jsx";
import api from "@/api/axios.js";


const MainLayout = () => {
  const [activeTabs, setActiveTabs] = useState(["dashboard"]);
  const [selectedTab, setSelectedTab] = useState("dashboard");
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [currentDate, setCurrentDate] = useState("");
  // const [appVersion, setAppVersion] = useState("1.0.0");
  const [isMobile, setIsMobile] = useState(false);



  const [userInfo, setUserInfo] = useState({
    full_name: "",
    profile_path: "",
    title:""
  });

  const [isUserModalOpen, setIsUserModalOpen] = useState(false);
  const [userName, setUserName] = useState("");
  const [profilePath, setProfilePath] = useState("");
  const [title, setTitle] = useState("");
  const navigate = useNavigate();



  const modules = [
    { id: "dashboard", title: "Dashboard", icon: <LayoutDashboard size={18} /> },
    { id: "stok", title: "Stok", icon: <PackageSearch size={18} /> },
    { id: "ayarlar", title: "Ayarlar", icon: <Settings size={18} /> }
  ];


  const moduleComponents = {
    dashboard: <Dashboard />
  };

  const openTab = (id) => {
    if (!activeTabs.includes(id)) {
      setActiveTabs([...activeTabs, id]);
    }
    setSelectedTab(id);
    if (isMobile) setSidebarOpen(false); // Mobilde menüyü otomatik kapat
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

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };


  useEffect(() => {

    const getUserProfile = async () => {

      const token = localStorage.getItem("token");
      if (!token) {
        navigate("/login");
        return;
      }

      try {
        const response = await api.put("/profile");
        setUserInfo(response.data);
        setUserName(response.data.full_name);
        setUserName(response.data.profile_path);
        setUserName(response.data.title);
      } catch (error) {
        console.error("Kullanıcı bilgileri alınırken hata oluştu:", error.response?.data || error.message);
        if (error.response?.status === 401) {
          navigate("/login");
        }
      }
    };

    // Kullanıcı adını localStorage'dan kontrol et
    const user = localStorage.getItem("userName");
    if (user) {
      setUserName(user);
    }

    // Tarih bilgisini ayarla
    const today = new Date();
    setCurrentDate(today.toLocaleDateString());

    // Ekran boyutuna göre ayarlamalar
    const handleResize = () => {
      const isMobileView = window.innerWidth < 1024;
      setIsMobile(isMobileView);
      setSidebarOpen(!isMobileView);
    };

    // Event listener'ları ekle
    window.addEventListener("resize", handleResize);
    handleResize(); // İlk çalıştırmada kontrol et

    // Profil bilgilerini çek
    getUserProfile();

    // Cleanup fonksiyonu
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, [navigate]);

  // Kullanıcı bilgilerini güncellemek için formdan gelen veriyi işle

  // const handleUserSubmit = (formData) => {
  //   setUserInfo(formData);
  //   setUserName(formData.name);
  //   setIsUserModalOpen(false);
  // };

  const handleUserSubmit = async (formData) => {
    console.log("API'ye Gönderilen Veriler:", formData); // Veriyi kontrol et
    try {
      const response = await api.put("/profile", formData); // API'ye PUT isteği gönder
      console.log("API'den Gelen Yanıt:", response.data); // API yanıtını kontrol et
      setUserInfo(response.data); // Güncellenen veriyi state'e kaydediyoruz
      setUserName(response.data.full_name); // Kullanıcı adını da güncelliyoruz
      setProfilePath(response.data.profile_path); // Kullanıcı adını da güncelliyoruz
      setTitle(response.data.title); // Kullanıcı adını da güncelliyoruz
      setIsUserModalOpen(false); // Modal'ı kapatıyoruz
    } catch (error) {
      console.error("Kullanıcı bilgileri güncellenirken hata oluştu:", error.response?.data || error.message);
    }
  };




  const toggleUserModal = () => {
    setIsUserModalOpen(!isUserModalOpen); // Modal'ı açıp kapat
  };


  return (
    <div className="flex flex-col h-screen bg-sky-50">
      {/* Top Bar */}
      <div className="bg-sky-500 text-white p-4 flex justify-between items-center shadow-sm">
        <div className="flex items-center">
          <button
            onClick={toggleSidebar}
            className="mr-4 text-white hover:bg-sky-400 p-2 rounded-full transition-colors"
          >
            {sidebarOpen ? <ChevronLeft size={24} /> : <ChevronRight size={24} />}
          </button>
          <div className="text-2xl font-bold text-white">Uygulama Adı</div>
        </div>
        <div className="flex items-center gap-4 text-lg text-sky-100">
          <button
            onClick={toggleUserModal} // Modal'ı tetikle
            className="flex items-center gap-2 hover:bg-sky-400 px-3 py-1 rounded transition-colors"
          >
            <User size={18} />
            <span>{userName || "Bilinmeyen Kullanıcı"}</span>
          </button>
          <button className="lg:hidden text-white" onClick={toggleSidebar}>
            ☰
          </button>
        </div>
      </div>

      <div className="flex flex-1 overflow-hidden">
        {/* Sidebar */}
        <aside
          className={`bg-sky-600 text-white flex flex-col transition-all duration-300 ease-in-out ${
            sidebarOpen ? "w-64" : "w-0"
          }`}
        >
          <div className={`p-4 flex flex-col gap-4 h-full ${!sidebarOpen && "hidden"}`}>
            <div  className="text-xl font-bold mb-6 text-sky-100">Modüller</div>
            {modules.map((mod) => (
              <button
                key={mod.id}
                onClick={() => openTab(mod.id)}
                className={`flex items-center gap-3 text-left p-3 rounded-lg text-sky-50 hover:bg-sky-500 transition-colors ${
                  selectedTab === mod.id ? "bg-sky-500" : ""
                }`}
              >
                {mod.icon}
                {mod.title}
              </button>
            ))}
            <div className="mt-auto">
              <button
                onClick={logout}
                className="flex items-center gap-2 bg-sky-500 hover:bg-sky-400 px-4 py-3 rounded-lg w-full text-white transition-colors"
              >
                <LogOut size={18} /> Çıkış Yap
              </button>
            </div>
          </div>
        </aside>

        {/* Main Area */}
        <div className="flex-1 flex flex-col bg-white">
          {/* Button Bar */}
          <div className="flex justify-end bg-white border-b p-3 gap-3">
            <button className="px-4 py-2 bg-cyan-400 text-white rounded-lg hover:bg-cyan-500 transition-colors shadow-sm">
              Buton 1
            </button>
            <button className="px-4 py-2 bg-teal-400 text-white rounded-lg hover:bg-teal-500 transition-colors shadow-sm">
              Buton 2
            </button>
            <button className="px-4 py-2 bg-sky-400 text-white rounded-lg hover:bg-sky-500 transition-colors shadow-sm">
              Buton 3
            </button>
          </div>

          <Tabs value={selectedTab} onValueChange={setSelectedTab} className="w-full h-full">
            <TabsList className="flex bg-white border-b p-2 gap-2 overflow-x-auto">
              {activeTabs.map((tab) => (
                <div
                  key={tab}
                  className={`flex items-center px-4 py-2 rounded-full transition-colors ${
                    selectedTab === tab ? "bg-sky-100 text-sky-700" : "bg-gray-50 text-gray-600"
                  }`}
                >
                  <TabsTrigger value={tab} className="text-sm font-medium mr-2">
                    {modules.find((m) => m.id === tab)?.title || tab}
                  </TabsTrigger>
                  <button onClick={() => closeTab(tab)} className="text-gray-500 hover:text-red-400">
                    ✕
                  </button>
                </div>
              ))}
            </TabsList>

            {activeTabs.map((tab) => (
              <TabsContent key={tab} value={tab} className="p-6 overflow-auto h-full bg-white">
                <motion.div initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.3 }}>
                  <div className="text-2xl font-bold mb-6 text-sky-700">{modules.find((m) => m.id === tab)?.title}</div>
                  <div className="text-lg text-gray-600">{moduleComponents[tab] || <p>Modül bulunamadı</p>}.</div>
                </motion.div>
              </TabsContent>
            ))}
          </Tabs>
        </div>
      </div>

      {/* Bottom Info Bar */}
      <div className="bg-sky-600 text-sky-100 p-3 flex justify-end w-full">
        <div className="flex flex-wrap justify-end gap-5 text-sm">
          {/*<span>Uygulama Versiyonu: {appVersion}</span>*/}
          <span>Uygulama Versiyonu: 2.0</span>
          <span>Form Versiyonu: 1.0</span>
          <span>Kullanıcı: {userName || "Bilinmeyen Kullanıcı"}</span>
          <span>Tarih: {currentDate}</span>
          <span className="font-medium text-cyan-200">e-Tıpsan Web | ⒸTıpsan</span>
        </div>
      </div>

      {/* User Modal */}
      {/*{isUserModalOpen && (*/}
      {/*    <GenericFormModal*/}
      {/*        isOpen={isUserModalOpen}*/}
      {/*        onClose={toggleUserModal}*/}
      {/*        title="Kullanıcı Bilgileri"*/}
      {/*        formFields={userFormFields}*/}
      {/*        initialData={userInfo}*/}
      {/*        onSubmit={handleUserSubmit}*/}
      {/*    />*/}
      {/*)}*/}

      <GenericFormModal
          isOpen={isUserModalOpen}
          onClose={() => setIsUserModalOpen(false)} // Modalı kapat
          onSubmit={handleUserSubmit} // Form submit işlemi
          initialData={userInfo} // Kullanıcı bilgileri modalda gösterilecek
      />

    </div>
  );
};

export default MainLayout;
