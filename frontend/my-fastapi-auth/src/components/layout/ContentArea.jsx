// ContentArea.jsx
import React from "react";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { motion } from "framer-motion";
import AltTabs from "@/components/layout/AltTabs.jsx";

const ContentArea = ({
                         activeTabs,
                         selectedTab,
                         setSelectedTab,
                         closeTab,
                         moduleComponents,
                         altTabs,
                         activeAltTab,
                         setActiveAltTab,
                     }) => {
    return (
        <div className="content flex-1 flex flex-col bg-white">
            {/* Ana Sekmeler */}
            <Tabs value={selectedTab} onValueChange={setSelectedTab} className="w-full h-full">
                <TabsList className="flex bg-white border-b p-2 gap-2 overflow-x-auto">
                    {activeTabs.map((tab) => (
                        <div
                            key={tab}
                            className={`flex items-center px-4 py-2 rounded-full transition-colors ${
                                selectedTab === tab ? "bg-sky-100 text-sky-700" : "bg-gray-50 text-gray-600"
                            }`}
                        >
                            <TabsTrigger value={tab} className="text-sm font-medium mr-2">
                                {tab}
                            </TabsTrigger>
                            <button onClick={() => closeTab(tab)} className="text-gray-500 hover:text-red-400">
                                ✕
                            </button>
                        </div>
                    ))}
                </TabsList>
                {activeTabs.map((tab) => (
                    <TabsContent key={tab} value={tab} className="p-6 overflow-auto h-full bg-white">
                        <motion.div
                            initial={{ opacity: 0, y: 10 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ duration: 0.3 }}
                        >
                            {moduleComponents[tab] || <p>Modül bulunamadı.</p>}
                        </motion.div>
                    </TabsContent>
                ))}
            </Tabs>

            {/* Alt Sekmeler */}
            {selectedTab === "kisiler" && altTabs["kisiler"]?.length > 0 && (
                <div className="border-b px-4 pt-2 bg-white">
                    <AltTabs
                        tabs={altTabs["kisiler"]}
                        activeAltTab={activeAltTab}
                        setActiveAltTab={setActiveAltTab}
                    />
                </div>
            )}
        </div>
    );
};

export default ContentArea;