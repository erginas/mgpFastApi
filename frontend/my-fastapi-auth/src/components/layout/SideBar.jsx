import React, { useEffect, useState } from "react";
import api from "@/api/axios.js";
import { useTabContext } from "@/contexts/TabContext"; // Context import
import * as Icons from "lucide-react"; // Tüm icon'ları tek objede alıyoruz

const Sidebar = ({ sidebarOpen }) => {
    const { selectedTab, openTab } = useTabContext(); // Context'ten verileri al
    const [menuItems, setMenuItems] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchMenuItems = async () => {
            try {
                const response = await api.get("/menu");
                setMenuItems(response.data);
            } catch (error) {
                console.error("Menü öğeleri alınırken hata oluştu:", error);
            } finally {
                setLoading(false);
            }
        };

        fetchMenuItems();
    }, []);

    if (loading) return <div>Yükleniyor...</div>;

    return (
        <div
            className={`sidebar bg-sky-600 text-white transition-all duration-300 ease-in-out ${
                sidebarOpen ? "w-64" : "w-0"
            }`}
        >
            <div className={`p-4 flex flex-col gap-4 h-full ${!sidebarOpen && "hidden"}`}>
                <div className="text-xl font-bold mb-6 text-sky-100">Modüller</div>

                <ul className="menu">
                    {menuItems.length === 0 ? (
                        <li className="menu-item">Menü Boş</li>
                    ) : (
                        menuItems.map((item) => {
                            const IconComponent = Icons[item.icon] || Icons.LayoutDashboard;

                            return (
                                <li key={item.id} className="menu-item">
                                    <button
                                        onClick={() => openTab(item.id, item.title)}
                                        className={`flex items-center gap-3 text-left p-3 rounded-lg text-sky-50 hover:bg-sky-500 transition-colors ${
                                            selectedTab === item.id ? "bg-sky-500" : ""
                                        }`}
                                    >
                                        <IconComponent size={18} />
                                        <span>{item.title}</span>
                                    </button>
                                </li>
                            );
                        })
                    )}
                </ul>
            </div>
        </div>
    );
};

export default Sidebar;
