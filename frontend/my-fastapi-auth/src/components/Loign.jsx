import React, { useState } from "react";
import api from "../api/axios.js";
import { Link } from "react-router-dom";  // Link import ediliyor
import logo from "../assets/react.svg";

// const Login = () => {
//     const [email, setEmail] = useState("");
//     const [password, setPassword] = useState("");
//
//     const handleLogin = async (e) => {
//         e.preventDefault();
//         try {
//             const response = await api.post("/login", {
//                 email,
//                 password,
//             });
//             console.log("Login success:", response.data);
//             // Token, yönlendirme, vs.
//         } catch (error) {
//             console.error("Login error:", error.response?.data || error.message);
//         }
//     };

const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(null); // Hata durumunu null olarak başlatıyoruz

    const handleLogin = async (e) => {
        e.preventDefault();
        setError(null); // Hata mesajını sıfırla

        try {
            const response = await api.post("/login", {
                email,
                password,
            });
            localStorage.setItem("token", response.data.token); //burasını kontrol et engin
            console.log("Login success:", response.data);
            // Token, yönlendirme, vs.
        } catch (error) {
            console.error("Login error:", error.response?.data || error.message);
            setError("Giriş yaparken bir hata oluştu.");
        }
    };

    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100">
            <form onSubmit={handleLogin} className="bg-white p-8 rounded shadow-md w-full max-w-sm">
                <h2 className="text-2xl font-semibold mb-6 text-center">Giriş Yap</h2>
                {/* LOGO */}
                <div className="flex justify-center mb-6">
                    <img src={logo} alt="Logo" className="h-16" />
                </div>
                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="w-full px-4 py-2 mb-4 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                />

                <input
                    type="password"
                    name="password"
                    placeholder="Şifre"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-full px-4 py-2 mb-4 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                />


                {error && <p className="text-red-500 mb-4 text-sm">{error}</p>}

                <div className="flex justify-between items-center mb-4">
                    <p className="text-sm text-gray-600">
                        <Link to="/forgot-password" className="text-blue-500 hover:text-blue-600">
                            Şifremi Unuttum
                        </Link>
                    </p>
                    <p className="text-sm text-gray-600">
                        Hesabınız yok mu?{" "}
                        <Link to="/register" className="text-blue-500 hover:text-blue-600">
                            Kayıt Ol
                        </Link>
                    </p>
                </div>

                <button
                    type="submit"
                    className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded"
                >
                    Giriş
                </button>
            </form>
        </div>
    );
};

export default Login;
