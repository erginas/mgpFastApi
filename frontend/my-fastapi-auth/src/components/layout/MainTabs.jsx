// MainTabs.jsx
import React, { useEffect } from "react";
import { useTabContext } from "@/contexts/TabContext";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs"; // UI kütüphanesini kullanalım

const MainTabs = () => {
    const { mainTabs, selectedTab, setSelectedTab, openTab, closeTab } = useTabContext();

    // Eğer tab yoksa, ilk sekmeyi aç
    useEffect(() => {
        if (mainTabs.length && !selectedTab) {
            openTab(mainTabs[0].id, mainTabs[0].title);  // İlk sekmeyi aktif yap
        }
    }, [mainTabs, selectedTab, openTab]);

    return (
        <Tabs value={selectedTab} onValueChange={setSelectedTab}>
            <TabsList>
                {mainTabs.map((tab) => (
                    <TabsTrigger
                        key={tab.id}
                        value={tab.id}
                        onClick={() => setSelectedTab(tab.id)}
                    >
                        {tab.title}
                    </TabsTrigger>
                ))}
            </TabsList>

            {mainTabs.map((tab) => (
                <TabsContent key={tab.id} value={tab.id}>
                    {tab.content}
                </TabsContent>
            ))}
        </Tabs>
    );
};

export default MainTabs;
