import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./components/Loign.jsx";
import Register from "./components/Register";
import ForgotPassword from "./components/ForgotPassword.jsx";
import Dashboard from "./components/dashboard/Dashboard.jsx";
import { TabProvider } from "@/contexts/TabContext.jsx";
import MainLayout from "./components/layout/MainLayout.jsx";
import KisiListesi from "@/pages/IK/KisiListesi.jsx";
import KisiDetay from "@/pages/IK/KisiDetay.jsx";
import KisiDuzenle from "@/pages/IK/KisiDuzenle.jsx";

function App() {
    return (
        <Router>
            <Routes>
                {/* Login, Register ve Forgot Password gibi giriş rotaları */}
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/forgot-password" element={<ForgotPassword />} />

                {/* MainLayout altında diğer alt yolları tanımlıyoruz */}
                <Route path="/" element={<MainLayout />}>
                    {/* Dashboard'a gitmek için alt rota */}
                    <Route path="dashboard" element={<Dashboard />} />

                    {/* Kişilerle ilgili alt yollar */}
                    <Route path="kisi/kisi-list" element={<KisiListesi />} />
                    {/*<Route path="ik/kisi-list" element={<KisiListesi />} />*/}
                    <Route path="ik/kisi-detay/:id" element={<KisiDetay />} />
                    <Route path="ik/kisi-duzenle/:id" element={<KisiDuzenle />} />
                </Route>
            </Routes>
        </Router>
    );
}

// TabProvider ile App'i sarıyoruz
const AppWithProvider = () => (
    <TabProvider>
        <App />
    </TabProvider>
);

export default AppWithProvider;
