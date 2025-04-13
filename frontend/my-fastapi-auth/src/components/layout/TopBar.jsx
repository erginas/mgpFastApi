// TopBar.jsx
import React from "react";
import { ChevronLeft, ChevronRight, User } from "lucide-react";

const TopBar = ({ sidebarOpen, toggleSidebar, userName, toggleUserModal }) => {
    return (
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
                    onClick={toggleUserModal}
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
    );
};

export default TopBar;