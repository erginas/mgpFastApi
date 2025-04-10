import React, { useEffect, useState } from "react";
import { X, Loader2 } from "lucide-react";

const GenericFormModal = ({
  isOpen,
  onClose,
  // title,
  // formFields,
  initialData,
  onSubmit,
  // submitButtonText = "Kaydet",
  // cancelButtonText = "İptal",
  // fetchData, // API'dan veri çekmek için fonksiyon
  // isLoading = false, // Yükleme durumu
  // error = null // Hata durumu
}) => {
  const [formData, setFormData] = useState(initialData || {});

  // useEffect(() => {
  //   if (isOpen) {
  //     if (fetchData) {
  //       // API'dan veri çek
  //       fetchData()
  //         .then(data => setFormData(data))
  //         .catch(error => console.error("API error:", error));
  //     } else if (initialData) {
  //       setFormData(initialData);
  //     } else {
  //       // Formu resetle
  //       setFormData({});
  //     }
  //   }
  // }, [isOpen, fetchData, initialData]);

  useEffect(() => {
    setFormData(initialData); // Modal açıldığında form verisini güncelle
  }, [isOpen, initialData]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  // const handleChange = (e) => {
  //   const { name, value } = e.target;
  //   setFormData(prev => ({ ...prev, [name]: value }));
  // };

  // const handleSubmit = (e) => {
  //   e.preventDefault();
  //   onSubmit(formData);
  // };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form submit edildi");  // Burada fonksiyon tetiklendiğini görmeliyiz
    console.log("Güncellenecek Veriler:", formData); // Form verisini kontrol et
    onSubmit(formData); // Formu submit et
  };

  if (!isOpen) return null;

//   return (
//     <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
//       <div className="bg-white rounded-lg shadow-xl w-full max-w-md">
//         <div className="flex justify-between items-center border-b p-4">
//           <h3 className="text-lg font-semibold text-sky-700">{title}</h3>
//           <button
//             onClick={onClose}
//             className="text-gray-500 hover:text-gray-700"
//             disabled={isLoading}
//           >
//             <X size={20} />
//           </button>
//         </div>
//
//         {isLoading ? (
//           <div className="p-6 flex justify-center items-center h-40">
//             <Loader2 className="animate-spin text-sky-500" size={30} />
//           </div>
//         ) : error ? (
//           <div className="p-6 text-red-500">
//             Veri yüklenirken hata oluştu: {error.message}
//           </div>
//         ) : (
//           <form onSubmit={handleSubmit}>
//             <div className="p-6 space-y-4">
//               {formFields.map((field) => (
//                 <div key={field.name}>
//                   <label className="block text-sm font-medium text-gray-700 mb-1">
//                     {field.label}
//                   </label>
//                   <input
//                     type={field.type || "text"}
//                     name={field.name}
//                     value={formData[field.name] || ""}
//                     onChange={handleChange}
//                     className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-sky-500"
//                     placeholder={field.placeholder}
//                     required={field.required}
//                     disabled={isLoading}
//                   />
//                 </div>
//               ))}
//             </div>
//             <div className="flex justify-end gap-3 p-4 border-t">
//               <button
//                 type="button"
//                 onClick={onClose}
//                 className="px-4 py-2 text-gray-700 hover:bg-gray-100 rounded-md transition-colors"
//                 disabled={isLoading}
//               >
//                 {cancelButtonText}
//               </button>
//               <button
//                 type="submit"
//                 className="px-4 py-2 bg-sky-500 text-white hover:bg-sky-600 rounded-md transition-colors disabled:opacity-50"
//                 disabled={isLoading}
//               >
//                 {isLoading ? (
//                   <span className="flex items-center gap-2">
//                     <Loader2 className="animate-spin" size={18} />
//                     İşleniyor...
//                   </span>
//                 ) : (
//                   submitButtonText
//                 )}
//               </button>
//             </div>
//           </form>
//         )}
//       </div>
//     </div>
//   );
// };

  return (
      isOpen && (
          <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
            <div className="bg-white p-6 rounded-md w-96">
              <h2 className="text-xl font-semibold mb-4">Kullanıcı Bilgilerini Düzenle</h2>
              <form onSubmit={handleSubmit}>

                <div className="mb-4">
                  <label htmlFor="full_name" className="block text-sm font-medium text-gray-700">Ad Soyad</label>
                  <input
                      type="text"
                      name="full_name"
                      value={formData.full_name || ""}
                      onChange={handleChange}
                      className="mt-1 p-2 w-full border border-gray-300 rounded-md"
                      required
                  />
                </div>

                <div className="mb-4">
                  <label htmlFor="email" className="block text-sm font-medium text-gray-700">profile path</label>
                  <input
                      type="text"
                      name="profile_path"
                      value={formData.profile_path || ""}
                      onChange={handleChange}
                      className="mt-1 p-2 w-full border border-gray-300 rounded-md"
                      required
                  />
                </div>

                <div className="mb-4">
                  <label htmlFor="department" className="block text-sm font-medium text-gray-700">title</label>
                  <input
                      type="text"
                      name="title"
                      value={formData.title || ""}
                      onChange={handleChange}
                      className="mt-1 p-2 w-full border border-gray-300 rounded-md"
                      required
                  />
                </div>

                {/*<div className="mb-4">*/}
                {/*  <label htmlFor="phone" className="block text-sm font-medium text-gray-700">Telefon</label>*/}
                {/*  <input*/}
                {/*      type="text"*/}
                {/*      name="phone"*/}
                {/*      value={formData.phone || ""}*/}
                {/*      onChange={handleChange}*/}
                {/*      className="mt-1 p-2 w-full border border-gray-300 rounded-md"*/}
                {/*      required*/}
                {/*  />*/}
                {/*</div>*/}

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