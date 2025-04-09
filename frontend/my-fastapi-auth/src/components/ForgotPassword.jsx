import React, { useState } from "react";
import api from "../api/axios.js";

const ForgotPassword = () => {
    const [email, setEmail] = useState("");
    const [message, setMessage] = useState("");

    const handlePasswordReset = async (e) => {
        e.preventDefault();
        try {
            // E-posta gönderimi
            const response = await api.post("/forgot-password", { email });

            // Yanıtı kontrol et
            console.log(response.data); // Backend'den gelen yanıtı kontrol edin.

            setMessage("Şifre sıfırlama bağlantısı e-posta adresinize gönderildi.");
        } catch (error) {
            console.error("Error:", error.response?.data || error.message);
            setMessage("Bir hata oluştu.");
        }
    };

    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100">
            <form
                onSubmit={handlePasswordReset}
                className="bg-white p-8 rounded shadow-md w-full max-w-sm"
            >
                <h2 className="text-2xl font-semibold mb-6 text-center">Şifreyi Sıfırla</h2>

                <input
                    type="email"
                    name="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="w-full px-4 py-2 mb-4 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                />

                {message && <p className="text-sm text-center mb-4">{message}</p>}

                <button
                    type="submit"
                    className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded"
                >
                    Sıfırlama Bağlantısı Gönder
                </button>
            </form>
        </div>
    );
};

export default ForgotPassword;
