import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:8000",
    withCredentials: true,
    headers: {
        "Content-Type": "application/json",
    },
});

// Axios interceptor ekleyerek Authorization başlığını her isteğe otomatik olarak ekleyebiliriz
api.interceptors.request.use((config) => {
    const token = localStorage.getItem("token"); // Token'ı localStorage'dan alıyoruz
    if (token) {
        config.headers["Authorization"] = `Bearer ${token}`; // Authorization başlığını ekliyoruz
    }
    return config;
}, (error) => {
    return Promise.reject(error);
});

export default api;