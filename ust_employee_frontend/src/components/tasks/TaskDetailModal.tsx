import React, { useState } from "react";
import { Task, Role, TaskStatus } from "@/types";
import { useTasks } from "@/contexts/TaskContext";
import { useAuth } from "@/contexts/AuthContext";
import { useEmployees } from "@/contexts/EmployeesContext";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Badge } from "@/components/ui/badge";
import {
  Calendar,
  User,
  Flag,
  Clock,
  MessageSquare,
  ArrowRight,
} from "lucide-react";
import { format } from "date-fns";

interface TaskDetailModalProps {
  task: Task;
  onClose: () => void;
  viewMode: Role;
}

const TaskDetailModal: React.FC<TaskDetailModalProps> = ({
  task,
  onClose,
  viewMode,
}) => {
  const { updateTaskStatus, assignTask, addRemark, remarks, deleteTask } =
    useTasks();
  const { user } = useAuth();
  const [newRemark, setNewRemark] = useState("");
  const [selectedAssignee, setSelectedAssignee] = useState(
    task.assigned_to || ""
  );
  const [selectedReviewer, setSelectedReviewer] = useState(task.reviewer || "");
  const { employees, getEmployeeById } = useEmployees();

  const taskRemarks = remarks.filter((r) => r.task_id === task.t_id);
  const assignee = task.assigned_to ? getEmployeeById(task.assigned_to) : null;
  const reviewer = task.reviewer ? getEmployeeById(task.reviewer) : null;
  const creator = getEmployeeById(task.created_by);

  const isReviewer = task.reviewer === user?.e_id;
  const canChangeStatus =
    viewMode !== "employee" || task.status === "IN_PROGRESS";
  const canAssign = viewMode === "admin" || viewMode === "manager";
  const canDelete = viewMode === "admin";

  const getNextStatus = (): TaskStatus | null => {
    if (viewMode === "employee" && task.status === "IN_PROGRESS")
      return "REVIEW";
    if (isReviewer && task.status === "REVIEW") return "DONE";
    return null;
  };

  const handleStatusChange = (newStatus: TaskStatus) => {
    if (
      task.status === "REVIEW" &&
      newStatus === "IN_PROGRESS" &&
      !newRemark.trim()
    ) {
      return;
    }
    updateTaskStatus(
      task.t_id,
      newStatus,
      user?.e_id || "",
      newRemark || undefined
    );
    setNewRemark("");
  };

  const handleAssign = () => {
    if (selectedAssignee) {
      assignTask(
        task.t_id,
        selectedAssignee,
        user?.e_id || "",
        selectedReviewer || undefined
      );
    }
  };

  const handleAddRemark = () => {
    if (newRemark.trim()) {
      addRemark(task.t_id, newRemark.trim(), user?.e_id || "");
      setNewRemark("");
    }
  };

  const handleDelete = () => {
    deleteTask(task.t_id);
    onClose();
  };

  const statusColors: Record<TaskStatus, string> = {
    TO_DO: "status-todo",
    IN_PROGRESS: "status-inprogress",
    REVIEW: "status-review",
    DONE: "status-done",
  };

  return (
    <Dialog open onOpenChange={onClose}>
      <DialogContent className="max-w-2xl max-h-[90vh] overflow-y-auto">
        <DialogHeader>
          <div className="flex items-start justify-between gap-4">
            <div>
              <span className="text-xs font-mono text-muted-foreground">
                {task.t_id}
              </span>
              <DialogTitle className="text-xl mt-1">{task.title}</DialogTitle>
            </div>
            <Badge className={`status-badge ${statusColors[task.status]}`}>
              {task.status.replace("_", " ")}
            </Badge>
          </div>
        </DialogHeader>

        <div className="space-y-6 mt-4">
          <div>
            <h4 className="text-sm font-medium text-foreground mb-2">
              Description
            </h4>
            <p className="text-sm text-muted-foreground">{task.description}</p>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div className="flex items-center gap-2 text-sm">
              <Flag className={`h-4 w-4 priority-${task.priority}`} />
              <span className="text-muted-foreground">Priority:</span>
              <span className="font-medium capitalize">{task.priority}</span>
            </div>
            <div className="flex items-center gap-2 text-sm">
              <Calendar className="h-4 w-4 text-muted-foreground" />
              <span className="text-muted-foreground">Due:</span>
              <span className="font-medium">
                {format(new Date(task.expected_closure), "MMM d, yyyy")}
              </span>
            </div>
            <div className="flex items-center gap-2 text-sm">
              <User className="h-4 w-4 text-muted-foreground" />
              <span className="text-muted-foreground">Assignee:</span>
              <span className="font-medium">
                {assignee?.name || "Unassigned"}
              </span>
            </div>
            <div className="flex items-center gap-2 text-sm">
              <User className="h-4 w-4 text-muted-foreground" />
              <span className="text-muted-foreground">Reviewer:</span>
              <span className="font-medium">{reviewer?.name || "Not set"}</span>
            </div>
          </div>

          {canAssign && task.status === "TO_DO" && (
            <div className="p-4 rounded-lg bg-muted/50 space-y-3">
              <h4 className="text-sm font-medium text-foreground">
                Assign Task
              </h4>
              <div className="grid grid-cols-2 gap-3">
                <Select
                  value={selectedAssignee}
                  onValueChange={setSelectedAssignee}
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Select assignee" />
                  </SelectTrigger>
                  <SelectContent>
                    {employees.map((emp) => (
                      <SelectItem key={emp.e_id} value={emp.e_id}>
                        {emp.name}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
                <Select
                  value={selectedReviewer}
                  onValueChange={setSelectedReviewer}
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Select reviewer" />
                  </SelectTrigger>
                  <SelectContent>
                    {employees
                      .filter(
                        (emp) =>
                          (emp.designation || "").includes("Manager") ||
                          (emp.designation || "").includes("Lead")
                      )
                      .map((emp) => (
                        <SelectItem key={emp.e_id} value={emp.e_id}>
                          {emp.name}
                        </SelectItem>
                      ))}
                  </SelectContent>
                </Select>
              </div>
              <Button
                onClick={handleAssign}
                disabled={!selectedAssignee}
                className="w-full"
              >
                Assign Task
              </Button>
            </div>
          )}

          {canChangeStatus && (
            <div className="p-4 rounded-lg bg-muted/50 space-y-3">
              <h4 className="text-sm font-medium text-foreground">
                Update Status
              </h4>
              {getNextStatus() && (
                <Button
                  onClick={() => handleStatusChange(getNextStatus()!)}
                  className="w-full"
                  disabled={
                    task.status === "REVIEW" &&
                    getNextStatus() === "IN_PROGRESS" &&
                    !newRemark.trim()
                  }
                >
                  Move to {getNextStatus()?.replace("_", " ")}
                  <ArrowRight className="ml-2 h-4 w-4" />
                </Button>
              )}
              {isReviewer && task.status === "REVIEW" && (
                <Button
                  variant="outline"
                  onClick={() => handleStatusChange("IN_PROGRESS")}
                  className="w-full"
                  disabled={!newRemark.trim()}
                >
                  Send Back to In Progress (Remark Required)
                </Button>
              )}
            </div>
          )}

          <div className="space-y-3">
            <h4 className="text-sm font-medium text-foreground flex items-center gap-2">
              <MessageSquare className="h-4 w-4" />
              Remarks ({taskRemarks.length})
            </h4>
            <div className="space-y-2 max-h-40 overflow-y-auto">
              {taskRemarks.map((remark) => {
                const author = getEmployeeById(remark.created_by);
                return (
                  <div
                    key={remark.id}
                    className="p-3 rounded-lg bg-muted/50 text-sm"
                  >
                    <div className="flex items-center justify-between mb-1">
                      <span className="font-medium text-foreground">
                        {author?.name}
                      </span>
                      <span className="text-xs text-muted-foreground">
                        {format(new Date(remark.created_at), "MMM d, HH:mm")}
                      </span>
                    </div>
                    <p className="text-muted-foreground">{remark.comment}</p>
                  </div>
                );
              })}
              {taskRemarks.length === 0 && (
                <p className="text-sm text-muted-foreground text-center py-4">
                  No remarks yet
                </p>
              )}
            </div>
            <div className="flex gap-2">
              <Textarea
                value={newRemark}
                onChange={(e) => setNewRemark(e.target.value)}
                placeholder="Add a remark..."
                className="min-h-[80px]"
              />
            </div>
            <Button
              onClick={handleAddRemark}
              variant="outline"
              disabled={!newRemark.trim()}
            >
              Add Remark
            </Button>
          </div>

          {canDelete && (
            <div className="pt-4 border-t">
              <Button
                variant="destructive"
                onClick={handleDelete}
                className="w-full"
              >
                Delete Task
              </Button>
            </div>
          )}
        </div>
      </DialogContent>
    </Dialog>
  );
};

export default TaskDetailModal;
