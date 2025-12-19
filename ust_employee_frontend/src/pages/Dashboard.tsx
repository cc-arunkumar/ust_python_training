import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "@/contexts/AuthContext";
import { Role } from "@/types";
import Header from "@/components/layout/Header";
import Sidebar from "@/components/layout/Sidebar";
import StatsCards from "@/components/dashboard/StatsCards";
import { useTasks } from "@/contexts/TaskContext";
import { LayoutGrid, Users } from "lucide-react";

const Dashboard: React.FC = () => {
  const { user, highestRole } = useAuth();
  const navigate = useNavigate();
  const [viewMode, setViewMode] = useState<Role>(highestRole);
  const { tasks } = useTasks();
  const [sidebarOpen, setSidebarOpen] = React.useState(true);

  const toggleSidebar = () => setSidebarOpen((prev) => !prev);
  const closeSidebar = () => setSidebarOpen(false);

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

  // derive basic counts for a small bar graph (reuse logic similar to StatsCards)
  const getFilteredTasks = () => {
    if (viewMode === "admin") return tasks;
    if (viewMode === "manager") {
      return tasks.filter(
        (t) =>
          t.created_by === user?.e_id ||
          t.assigned_by === user?.e_id ||
          t.reviewer === user?.e_id
      );
    }
    return tasks.filter((t) => t.assigned_to === user?.e_id);
  };

  const filteredTasks = getFilteredTasks();
  const counts = {
    todo: filteredTasks.filter((t) => t.status === "TO_DO").length,
    inProgress: filteredTasks.filter((t) => t.status === "IN_PROGRESS").length,
    review: filteredTasks.filter((t) => t.status === "REVIEW").length,
    done: filteredTasks.filter((t) => t.status === "DONE").length,
  };

  return (
    <div className="min-h-screen bg-background">
      <Header
        currentView={viewMode}
        onViewChange={setViewMode}
        onToggleSidebar={toggleSidebar}
        // sidebarOpen={sidebarOpen}
      />

      <div className="flex">
        <Sidebar
          isOpen={sidebarOpen}
          onToggle={toggleSidebar}
          onClose={closeSidebar}
        />

        <main className="flex-1">
          <StatsCards viewMode={viewMode} />

          <section className="p-6">
            <h2 className="text-lg font-semibold mb-3">Task Overview</h2>
            <div className="w-full max-w-2xl">
              <div className="flex items-end gap-4 h-40">
                <div className="flex flex-col items-center gap-2 w-1/4">
                  <div className="w-full bg-muted/30 h-full flex items-end rounded">
                    <div
                      className="bg-[hsl(var(--status-todo))] w-full"
                      style={{ height: `${Math.max(8, counts.todo * 12)}px` }}
                    />
                  </div>
                  <span className="text-xs">To Do </span>
                </div>

                <div className="flex flex-col items-center gap-2 w-1/4">
                  <div className="w-full bg-muted/30 h-full flex items-end rounded">
                    <div
                      className="bg-[hsl(var(--status-inprogress))] w-full"
                      style={{
                        height: `${Math.max(8, counts.inProgress * 12)}px`,
                      }}
                    />
                  </div>
                  <span className="text-xs">In Progress</span>
                </div>

                <div className="flex flex-col items-center gap-2 w-1/4">
                  <div className="w-full bg-muted/30 h-full flex items-end rounded">
                    <div
                      className="bg-[hsl(var(--status-review))] w-full"
                      style={{ height: `${Math.max(8, counts.review * 12)}px` }}
                    />
                  </div>
                  <span className="text-xs">Review </span>
                </div>

                <div className="flex flex-col items-center gap-2 w-1/4">
                  <div className="w-full bg-muted/30 h-full flex items-end rounded">
                    <div
                      className="bg-[hsl(var(--status-done))] w-full"
                      style={{ height: `${Math.max(8, counts.done * 12)}px` }}
                    />
                  </div>
                  <span className="text-xs">Done </span>
                </div>
              </div>
            </div>
          </section>

          {/* Quick links to task board or employees */}
          <section className="p-6">
            {showEmployees ? (
              <p className="text-sm text-muted-foreground">
                Use the sidebar to view Tasks or Employees pages.
              </p>
            ) : (
              <p className="text-sm text-muted-foreground">
                Use the sidebar to go to the Task Board.
              </p>
            )}
          </section>
        </main>
      </div>
    </div>
  );
};

export default Dashboard;
