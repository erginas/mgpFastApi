import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";
import { User, Package, Activity } from "lucide-react";

const data = [
  { name: "Pzt", değer: 30 },
  { name: "Sal", değer: 45 },
  { name: "Çar", değer: 28 },
  { name: "Per", değer: 60 },
  { name: "Cum", değer: 40 },
  { name: "Cmt", değer: 35 },
  { name: "Paz", değer: 50 },
];

const Dashboard = () => {
  return (
    <div className="p-4 space-y-6">
      <h2 className="text-2xl font-bold">Hoş geldiniz!</h2>

      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <Card className="shadow-md">
          <CardContent className="flex items-center space-x-4 p-4">
            <User className="text-blue-500" />
            <div>
              <p className="text-sm text-muted-foreground">Toplam Kullanıcı</p>
              <p className="text-xl font-semibold">124</p>
            </div>
          </CardContent>
        </Card>
        <Card className="shadow-md">
          <CardContent className="flex items-center space-x-4 p-4">
            <Package className="text-green-500" />
            <div>
              <p className="text-sm text-muted-foreground">Toplam Stok</p>
              <p className="text-xl font-semibold">876</p>
            </div>
          </CardContent>
        </Card>
        <Card className="shadow-md">
          <CardContent className="flex items-center space-x-4 p-4">
            <Activity className="text-orange-500" />
            <div>
              <p className="text-sm text-muted-foreground">Bugünkü İşlem</p>
              <p className="text-xl font-semibold">42</p>
            </div>
          </CardContent>
        </Card>
      </div>

      <Card className="shadow-md">
        <CardContent className="p-4">
          <h3 className="text-lg font-semibold mb-4">Haftalık İşlem Grafiği</h3>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={data}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="değer" stroke="#8884d8" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </div>
  );
};

export default Dashboard;
