import React, { useState } from "react";
import api from "../api/axios.js";
import logo from "../assets/react.svg"

const Register = () => {
    const [fullName, setFullName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [error, setError] = useState("");
    const [successMessage, setSuccessMessage] = useState("");

    const handleRegister = async (e) => {
        e.preventDefault();
        setError(""); // Hata mesajlarını sıfırla
        setSuccessMessage(""); // Başarı mesajını sıfırla

        // Şifreler eşleşiyor mu kontrol et
        if (password !== confirmPassword) {
            setError("Şifreler eşleşmiyor.");
            return;
        }

        try {
            const response = await api.post("/register", {
                full_name: fullName,
                email,
                password,
                confirm_password: confirmPassword, // confirm_password de gönderilmeli
            });
            console.log("Registration success:", response.data);
            setSuccessMessage("Kayıt başarılı! Lütfen giriş yapın.");
            // Başarılı kayıt sonrası yapılacak işlemler (örn. yönlendirme)
        } catch (error) {
            console.error("Registration error:", error.response?.data || error.message);
            setError("Kayıt sırasında bir hata oluştu.");
        }
    };

    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100">
            <form
                onSubmit={handleRegister}
                className="bg-white p-8 rounded shadow-md w-full max-w-sm"
            >
                <h2 className="text-2xl font-semibold mb-6 text-center">Kayıt Ol</h2>

                {/* LOGO */}
                <div className="flex justify-center mb-6">
                    <img src={logo} alt="Logo" className="h-16" />
                </div>

                <input
                    type="text"
                    name="full_name"
                    placeholder="Tam Adınız"
                    value={fullName}
                    onChange={(e) => setFullName(e.target.value)}
                    className="w-full px-4 py-2 mb-4 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                />

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

                <input
                    type="password"
                    name="confirm_password"
                    placeholder="Şifreyi Onayla"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    className="w-full px-4 py-2 mb-4 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    required
                />

                {error && <p className="text-red-500 mb-4 text-sm">{error}</p>}
                {successMessage && (
                    <p className="text-green-500 mb-4 text-sm">{successMessage}</p>
                )}

                <button
                    type="submit"
                    className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded"
                >
                    Kayıt Ol
                </button>



                <p className="mt-4 text-center text-sm">
                    Zaten hesabınız var mı?{" "}
                    <a href="/" className="text-blue-500 hover:underline">
                        Giriş Yapın
                    </a>
                </p>
            </form>
        </div>
    );
};

export default Register;
