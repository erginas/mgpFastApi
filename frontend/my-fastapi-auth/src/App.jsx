import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./components/Loign.jsx";
import Register from "./components/Register";
import ForgotPassword from "./components/ForgotPassword.jsx";
import Dashboard from "./components/dashboard/Dashboard.jsx";// Dashboard bileşenini import ediyoruz
import MainLayout from "./components/main/MainLayout.jsx";
import KisiDuzenle from "@/pages/IK/KisiDuzenle.jsx";
import KisiListesi from "@/pages/IK/KisiListesi.jsx";
import KisiDetay from "@/pages/IK/KisiDetay.jsx";

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Login />} />
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />
                <Route path="/forgot-password" element={<ForgotPassword />} />
                <Route path="/MainLayout" element={<MainLayout />} />  {/* Dashboard sayfası */}
                <Route path="/dashboard" element={<Dashboard />} />  {/* Dashboard sayfası */}
                <Route path="/ik/kisi-list" element={<KisiListesi />} />
                <Route path="/ik/kisi-detay/:id" element={<KisiDetay />} />
                <Route path="/ik/kisi-duzenle/:id" element={<KisiDuzenle />} />
            </Routes>
        </Router>
    );
}

export default App;
