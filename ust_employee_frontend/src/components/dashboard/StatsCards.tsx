import React from "react";
import { Task, Role } from "@/types";
import { useTasks } from "@/contexts/TaskContext";
import { useAuth } from "@/contexts/AuthContext";
import { Card, CardContent } from "@/components/ui/card";
import {
  ListTodo,
  Clock,
  Eye,
  CheckCircle2,
  TrendingUp,
  AlertTriangle,
} from "lucide-react";

interface StatsCardsProps {
  viewMode: Role;
}

const StatsCards: React.FC<StatsCardsProps> = ({ viewMode }) => {
  const { tasks } = useTasks();
  const { user } = useAuth();

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
  const todoCount = filteredTasks.filter((t) => t.status === "TO_DO").length;
  const inProgressCount = filteredTasks.filter(
    (t) => t.status === "IN_PROGRESS"
  ).length;
  const reviewCount = filteredTasks.filter((t) => t.status === "REVIEW").length;
  const doneCount = filteredTasks.filter((t) => t.status === "DONE").length;
  const highPriorityCount = filteredTasks.filter(
    (t) => t.priority === "high" && t.status !== "DONE"
  ).length;

  const stats = [
    {
      label: "To Do",
      value: todoCount,
      icon: ListTodo,
      color: "text-[hsl(var(--status-todo))]",
      bg: "bg-[hsl(var(--status-todo-bg))]",
    },
    {
      label: "In Progress",
      value: inProgressCount,
      icon: Clock,
      color: "text-[hsl(var(--status-inprogress))]",
      bg: "bg-[hsl(var(--status-inprogress-bg))]",
    },
    {
      label: "In Review",
      value: reviewCount,
      icon: Eye,
      color: "text-[hsl(var(--status-review))]",
      bg: "bg-[hsl(var(--status-review-bg))]",
    },
    {
      label: "Completed",
      value: doneCount,
      icon: CheckCircle2,
      color: "text-[hsl(var(--status-done))]",
      bg: "bg-[hsl(var(--status-done-bg))]",
    },
    {
      label: "High Priority",
      value: highPriorityCount,
      icon: AlertTriangle,
      color: "text-[hsl(var(--priority-high))]",
      bg: "bg-[hsl(var(--priority-high))]/10",
    },
  ];

  return (
    <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 p-6 pb-0">
      {stats.map((stat) => (
        <Card key={stat.label} className="relative overflow-hidden">
          <CardContent className="p-4">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-muted-foreground">{stat.label}</p>
                <p className="text-2xl font-bold text-foreground mt-1">
                  {stat.value}
                </p>
              </div>
              <div className={`p-3 rounded-xl ${stat.bg}`}>
                <stat.icon className={`h-5 w-5 ${stat.color}`} />
              </div>
            </div>
          </CardContent>
        </Card>
      ))}
    </div>
  );
};

export default StatsCards;
