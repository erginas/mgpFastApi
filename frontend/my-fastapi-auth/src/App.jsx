import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./components/Loign.jsx";
import Register from "./components/Register";
import ForgotPassword from "./components/ForgotPassword.jsx";
import Dashboard from "./components/dashboard/Dashboard.jsx";// Dashboard bileşenini import ediyoruz
import MainLayout from "./components/main/MainLayout.jsx";

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
            </Routes>
        </Router>
    );
}

export default App;
