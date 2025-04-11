import React, {useEffect, useState} from "react";
import {X, Loader2} from "lucide-react";

const GenericFormModal = ({
                              isOpen,
                              onClose,
                              onSubmit,
                              initialValues
                          }) => {
    const [formData, setFormData] = useState({
        full_name: "",
        title: "",
        profile_path: ""
    });


    useEffect(() => {
        console.log("Initial values geldi:", initialValues);

        if (initialValues) {
            console.log("Initial values received:", initialValues);
            setFormData({
                full_name: initialValues.full_name || '',
                title: initialValues.title || '',
                profile_path: initialValues.profile_path || ''
            });
        }
    }, [initialValues]);

    const handleChange = (e) => {
        const {name, value} = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log("Form submit edildi");  // Burada fonksiyon tetiklendiğini görmeliyiz
        console.log("Güncellenecek Veriler:", formData); // Form verisini kontrol et
        onSubmit(formData); // Formu submit et
    };

    if (!isOpen) return null;

    return (
        isOpen && (
            <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
                <div className="bg-white p-6 rounded-md w-96">
                    <h2 className="text-xl font-semibold mb-4">Kullanıcı Bilgilerini Düzenle</h2>
                    <form onSubmit={handleSubmit}>

                        <div className="mb-4">
                            <label htmlFor="full_name" className="block text-sm font-medium text-gray-700">Ad
                                Soyad</label>
                            <input
                                type="text"
                                name="full_name"
                                value={formData.full_name || ""}
                                onChange={(e) => setFormData({...formData, full_name: e.target.value})}
                                className="mt-1 p-2 w-full border border-gray-300 rounded-md"
                                required
                            />
                        </div>

                        <div className="mb-4">
                            <label htmlFor="email" className="block text-sm font-medium text-gray-700">profile
                                path</label>
                            <input
                                type="text"
                                name="profile_path"
                                value={formData.profile_path || ""}
                                onChange={(e) => setFormData({...formData, profile_path: e.target.value})}
                                className="mt-1 p-2 w-full border border-gray-300 rounded-md"
                                required
                            />
                        </div>

                        <div className="mb-4">
                            <label htmlFor="department"
                                   className="block text-sm font-medium text-gray-700">title</label>
                            <input
                                type="text"
                                name="title"
                                value={formData.title || ""}
                                onChange={(e) => setFormData({...formData, title: e.target.value})}
                                className="mt-1 p-2 w-full border border-gray-300 rounded-md"
                                required
                            />
                        </div>

                        <div className="flex justify-between">
                            <button
                                type="button"
                                onClick={onClose}
                                className="px-4 py-2 bg-gray-300 rounded-md"
                            >
                                Kapat
                            </button>
                            <button
                                type="submit"
                                className="px-4 py-2 bg-blue-500 text-white rounded-md"
                            >
                                Güncelle
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        )
    );
};

export default GenericFormModal;