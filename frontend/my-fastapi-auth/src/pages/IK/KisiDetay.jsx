const KisiDetay = ({ user }) => {
    if (!user) {
        return <p className="text-center mt-10">Kullanıcı bilgisi bulunamadı.</p>;
    }

    return (
        <div className="p-6">
            <h2 className="text-2xl font-bold mb-4">Kişi Detay</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <h2 className="text-xl font-bold mb-4">{user.ADI} {user.SOYADI} Detayları</h2>
                <div><strong>Ad:</strong> {user.ADI}</div>
                <div><strong>Soyad:</strong> {user.SOYADI}</div>
                <div><strong>Kimlik No:</strong> {user.KIMLIK_NO}</div>
                <div><strong>Meslek:</strong> {user.MESLEGI}</div>
                <div><strong>Telefon:</strong> {user.CEP_TEL}</div>
                <div><strong>Adres:</strong> {user.ADRES}</div>
                <div><strong>Doğum Tarihi:</strong> {user.DOGUM_TARIHI?.split("T")[0]}</div>
                <div><strong>Birim No:</strong> {user.BIRIM_NO}</div>
                <div><strong>İşe Giriş:</strong> {user.ISE_GIRIS_TARIHI?.split("T")[0]}</div>
            </div>

            <div className="mt-6 flex gap-4">
                <Link
                    to="/ik/kisi-list"
                    className="text-blue-500 hover:text-blue-700 underline"
                >
                    ← Geri Dön
                </Link>
                <Link
                    to={`/ik/kisi-duzenle/${user.ID}`}
                    className="text-green-600 hover:text-green-800 underline"
                >
                    ✏️ Düzenle
                </Link>
            </div>
        </div>
    );
};
