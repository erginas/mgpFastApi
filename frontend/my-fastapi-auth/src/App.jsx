import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./components/Loign.jsx";
import Register from "./components/Register"; // Register sayfası
import ForgotPassword from "./components/ForgotPassword.jsx";


function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Login />} />  {/* Login sayfası */}
                <Route path="/register" element={<Register />} />  {/* Register sayfası */}
                <Route path="/forgot-password" element={<ForgotPassword />} />  {/* Forgot sayfası */}
            </Routes>
        </Router>
    );
}

export default App;