const handleUserSubmit = async (formData) => {
    console.log("API'ye Gönderilen Veriler:", formData); // Veriyi kontrol et
    try {
        const response = await api.put("/profile", formData); // API'ye PUT isteği gönder
        console.log("API'den Gelen Yanıt:", response.data); // API yanıtını kontrol et
        setUserInfo(response.data); // Güncellenen veriyi state'e kaydediyoruz
        setUserName(response.data.name); // Kullanıcı adını da güncelliyoruz
        setIsUserModalOpen(false); // Modal'ı kapatıyoruz
    } catch (error) {
        console.error("Kullanıcı bilgileri güncellenirken hata oluştu:", error.response?.data || error.message);
    }
};