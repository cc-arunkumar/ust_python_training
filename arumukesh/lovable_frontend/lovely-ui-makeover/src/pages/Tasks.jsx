import React from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import KanbanBoard from "../components/tasks/KanbanBoard";
import Button from "../components/common/Button";
import { PlusCircle } from "lucide-react";

const Tasks = () => {
  const { isAdmin, isManager } = useAuth();

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Tasks</h1>
          <p className="text-gray-600 mt-1">Manage and track all tasks</p>
        </div>
        {(isAdmin() || isManager()) && (
          <Link to="/tasks/create">
            <Button>
              <PlusCircle className="w-4 h-4 mr-2" />
              Create Task
            </Button>
          </Link>
        )}
      </div>

      <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
        <p className="text-sm text-blue-800">
          <strong>Tip:</strong> Drag and drop tasks between columns to update
          their status. You can only move tasks that you're assigned to or
          reviewing.
        </p>
      </div>

      <KanbanBoard />
    </div>
  );
};

export default Tasks;
