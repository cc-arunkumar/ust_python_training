import React, { useState, useEffect } from "react";
import Header from "@/components/layout/Header";
import Sidebar from "@/components/layout/Sidebar";
import TaskBoard from "@/components/tasks/TaskBoard";
import { Role } from "@/types";
import { useAuth } from "@/contexts/AuthContext";

const TasksPage: React.FC = () => {
  const { highestRole, user } = useAuth();
  const [viewMode, setViewMode] = useState<Role>(highestRole);
  const [sidebarOpen, setSidebarOpen] = useState(true);

  useEffect(() => {
    setViewMode(highestRole);
  }, [highestRole]);

  if (!user) return null;

  return (
    <div className="min-h-screen bg-background">
      <Header
        currentView={viewMode}
        onViewChange={setViewMode}
        onToggleSidebar={() => setSidebarOpen((s) => !s)}
        // sidebarOpen={sidebarOpen}
      />
      <div className="flex">
        <Sidebar
          isOpen={sidebarOpen}
          onClose={() => setSidebarOpen(false)}
          onToggle={() => setSidebarOpen((s) => !s)}
        />
        <main className="flex-1">
          <TaskBoard viewMode={viewMode} />
        </main>
      </div>
    </div>
  );
};

export default TasksPage;
