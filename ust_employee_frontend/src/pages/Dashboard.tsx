import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "@/contexts/AuthContext";
import { Role } from "@/types";
import Header from "@/components/layout/Header";
import StatsCards from "@/components/dashboard/StatsCards";
import TaskBoard from "@/components/tasks/TaskBoard";
import EmployeeList from "@/components/employees/EmployeeList";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { LayoutGrid, Users } from "lucide-react";

const Dashboard: React.FC = () => {
  const { user, highestRole } = useAuth();
  const navigate = useNavigate();
  const [viewMode, setViewMode] = useState<Role>(highestRole);
  const [activeTab, setActiveTab] = useState("tasks");

  useEffect(() => {
    if (!user) {
      navigate("/login");
    }
  }, [user, navigate]);

  useEffect(() => {
    setViewMode(highestRole);
  }, [highestRole]);

  if (!user) return null;

  const showEmployees = viewMode === "admin" || viewMode === "manager";

  return (
    <div className="min-h-screen bg-background">
      <Header currentView={viewMode} onViewChange={setViewMode} />

      <main>
        <StatsCards viewMode={viewMode} />

        {showEmployees ? (
          <div className="p-6">
            <Tabs value={activeTab} onValueChange={setActiveTab}>
              <TabsList className="mb-4">
                <TabsTrigger value="tasks" className="flex items-center gap-2">
                  <LayoutGrid className="h-4 w-4" />
                  Task Board
                </TabsTrigger>
                <TabsTrigger
                  value="employees"
                  className="flex items-center gap-2"
                >
                  <Users className="h-4 w-4" />
                  Employees
                </TabsTrigger>
              </TabsList>

              <TabsContent value="tasks" className="-mx-6 -mt-2">
                <TaskBoard viewMode={viewMode} />
              </TabsContent>

              <TabsContent value="employees" className="-mx-6 -mt-2">
                <EmployeeList viewMode={viewMode} />
              </TabsContent>
            </Tabs>
          </div>
        ) : (
          <TaskBoard viewMode={viewMode} />
        )}
      </main>
    </div>
  );
};

export default Dashboard;
