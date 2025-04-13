import React from "react";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";

const AltTabs = ({ tabs, activeAltTab, setActiveAltTab }) => {
    if (!tabs || tabs.length === 0) return null;

    return (
        <div className="mt-4">
            <Tabs value={activeAltTab} onValueChange={setActiveAltTab}>
                <TabsList className="flex gap-2 bg-sky-100 p-2 rounded shadow">
                    {tabs.map((tab) => (
                        <TabsTrigger key={tab.key} value={tab.key}>
                            {tab.label}
                        </TabsTrigger>
                    ))}
                </TabsList>

                {tabs.map((tab) => (
                    <TabsContent key={tab.key} value={tab.key}>
                        {tab.component}
                    </TabsContent>
                ))}
            </Tabs>
        </div>
    );
};

export default AltTabs;
