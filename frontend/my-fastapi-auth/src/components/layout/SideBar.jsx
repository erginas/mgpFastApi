// Sidebar.jsx
import React from "react";
import { LayoutDashboard, PackageSearch, Settings, User } from "lucide-react";

const Sidebar = ({ modules, sidebarOpen, selectedTab, openTab }) => {
    return (
        <div
            className={`sidebar bg-sky-600 text-white transition-all duration-300 ease-in-out ${
                sidebarOpen ? "w-64" : "w-0"
            }`}
        >
            <div className={`p-4 flex flex-col gap-4 h-full ${!sidebarOpen && "hidden"}`}>
                <div className="text-xl font-bold mb-6 text-sky-100">Modüller</div>
                {modules.map((mod) => (
                    <button
                        key={mod.id}
                        onClick={() => openTab(mod.id, mod.title)}
                        className={`flex items-center gap-3 text-left p-3 rounded-lg text-sky-50 hover:bg-sky-500 transition-colors ${
                            selectedTab === mod.id ? "bg-sky-500" : ""
                        }`}
                    >
                        {mod.icon}
                        {mod.title}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default Sidebar;