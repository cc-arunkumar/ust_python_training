import React, { useState, useEffect } from "react";
import { taskService } from "@/services/taskService";
import { mapBackendTaskToFrontend } from "@/lib/utils";
import KanbanBoard from "@/components/tasks/KanbanBoard";
import { Task, TaskStatus, Priority } from "@/types";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Badge } from "@/components/ui/badge";
import { useAuth } from "@/context/AuthContext";
import { employeeService } from "@/services/employeeService";
import { useToast } from "@/hooks/use-toast";
import { format } from "date-fns";
import { remarkService } from "@/services/remarkService";
import {
  Search,
  Filter,
  Calendar,
  User,
  MessageSquare,
  Clock,
} from "lucide-react";

const TaskBoard: React.FC = () => {
  const { currentRole, user } = useAuth();
  const { toast } = useToast();
  const [tasks, setTasks] = useState<Task[]>([]);
  // simplified: no manager view modes — always show fetched tasks
  const [employeeNames, setEmployeeNames] = useState<Record<string, string>>(
    {}
  );
  const [employeeDetails, setEmployeeDetails] = useState<
    Record<
      string,
      { name: string; designation?: string; mgr_id?: number; mgr_name?: string }
    >
  >({});

  useEffect(() => {
    let mounted = true;
    const fetchTasks = async () => {
      if (!user?.id) return;
      try {
        const backendRoleMap: { [k: string]: string } = {
          admin: "Admin",
          manager: "Manager",
          developer: "Developer",
        };
        const backendRole = backendRoleMap[currentRole] || "Developer";
        const e_id = parseInt(user.id, 10);
        let backendTasksRaw: any[] = [];

        if (currentRole === "manager") {
          // Managers' My Tasks should show only tasks assigned to them
          const resp = await taskService.getTasks(
            1,
            1000,
            undefined,
            undefined,
            backendRole
          );
          const all = resp.data || [];
          backendTasksRaw = all.filter((t: any) => t.assigned_to === e_id);
        } else if (currentRole === "admin") {
          // Admin sees all tasks
          const resp = await taskService.getTasks(
            1,
            1000,
            undefined,
            undefined,
            backendRole
          );
          backendTasksRaw = resp.data || [];
        } else {
          // Developer/other roles: show tasks assigned to this user
          backendTasksRaw = await taskService.getMyTasks(e_id, backendRole);
        }

        if (!mounted) return;
        const frontTasksAll = backendTasksRaw.map(mapBackendTaskToFrontend);
        // Keep all tasks in state for manager so we can switch views client-side
        // Show all fetched tasks directly (removed created/assigned/reviewer filters)
        setTasks(frontTasksAll);
      } catch (err) {
        console.error("Error fetching tasks", err);
      }
    };

    fetchTasks();

    return () => {
      mounted = false;
    };
  }, [user?.id, currentRole]);

  const getEmployeeName = async (id?: string) => {
    if (!id) return undefined;
    if (employeeNames[id]) return employeeNames[id];
    try {
      const backendRoleMap: { [k: string]: string } = {
        admin: "Admin",
        manager: "Manager",
        developer: "Developer",
      };
      const backendRole = backendRoleMap[currentRole] || "Developer";
      const emp = await employeeService.getEmployeeCached(
        parseInt(id, 10),
        backendRole
      );
      setEmployeeNames((s) => ({ ...s, [id]: emp.name }));
      setEmployeeDetails((s) => ({
        ...s,
        [id]: {
          name: emp.name,
          designation: emp.designation,
          mgr_id: emp.mgr_id,
        },
      }));
      // populate manager name if available
      if (emp.mgr_id) {
        try {
          const mgr = await employeeService.getEmployeeCached(
            emp.mgr_id,
            backendRole
          );
          setEmployeeDetails((s) => ({
            ...s,
            [id]: {
              name: s[id]?.name || emp.name || "",
              designation: s[id]?.designation || emp.designation,
              mgr_id: s[id]?.mgr_id || emp.mgr_id,
              mgr_name: mgr.name,
            },
          }));
        } catch (e) {
          // ignore
        }
      }
      return emp.name;
    } catch (err) {
      return undefined;
    }
  };

  const [searchQuery, setSearchQuery] = useState("");
  const [priorityFilter, setPriorityFilter] = useState<Priority | "all">("all");
  const [selectedTask, setSelectedTask] = useState<Task | null>(null);
  const [remarks, setRemarks] = useState<any[]>([]);
  const [loadingRemarks, setLoadingRemarks] = useState(false);
  const [newRemark, setNewRemark] = useState("");
  const [remarkFile, setRemarkFile] = useState<File | null>(null);

  // When a task is selected, ensure we populate employee names and load remarks
  useEffect(() => {
    if (!selectedTask) return;
    (async () => {
      if (selectedTask.assignedTo) {
        await getEmployeeName(selectedTask.assignedTo);
      }
      if (selectedTask.reviewer) {
        await getEmployeeName(selectedTask.reviewer);
      }
    })();

    const loadRemarks = async () => {
      try {
        setLoadingRemarks(true);
        const backendRoleMap: { [k: string]: string } = {
          admin: "Admin",
          manager: "Manager",
          developer: "Developer",
        };
        const backendRole = backendRoleMap[currentRole] || "Developer";
        const r = await remarkService.getRemarksByTask(
          parseInt(selectedTask.id, 10),
          backendRole
        );
        setRemarks(r || []);
      } catch (err) {
        console.error("Failed to load remarks", err);
        setRemarks([]);
      } finally {
        setLoadingRemarks(false);
      }
    };
    loadRemarks();
  }, [selectedTask]);

  // Filter tasks (simplified: do not expose created/assigned/reviewer/all filters)
  const filteredTasks = tasks.filter((task) => {
    const matchesSearch =
      task.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      task.id.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesPriority =
      priorityFilter === "all" || task.priority === priorityFilter;
    return matchesSearch && matchesPriority;
  });

  const handleTaskClick = (task: Task) => {
    setSelectedTask(task);
  };

  const [isEditingTask, setIsEditingTask] = useState(false);
  const [editForm, setEditForm] = useState({
    title: "",
    description: "",
    priority: "medium",
    expectedClosure: "",
  });

  const startEdit = () => {
    if (!selectedTask) return;
    setEditForm({
      title: selectedTask.title,
      description: selectedTask.description,
      priority: selectedTask.priority,
      expectedClosure: selectedTask.expectedClosure,
    });
    setIsEditingTask(true);
  };

  const saveEdit = async () => {
    if (!selectedTask) return;
    try {
      const backendRoleMap: { [k: string]: string } = {
        admin: "Admin",
        manager: "Manager",
        developer: "Developer",
      };
      const backendRole = backendRoleMap[currentRole] || "Manager";
      const payload: any = {
        title: editForm.title,
        description: editForm.description,
        priority: editForm.priority,
        expected_closure: editForm.expectedClosure,
      };
      await taskService.updateTask(
        parseInt(selectedTask.id, 10),
        payload,
        backendRole
      );

      // Update local state
      const updatedAt = new Date().toISOString();
      setTasks((prev) =>
        prev.map((t) =>
          t.id === selectedTask.id
            ? {
                ...t,
                title: editForm.title,
                description: editForm.description,
                priority: editForm.priority as any,
                expectedClosure: editForm.expectedClosure,
                updatedAt,
              }
            : t
        )
      );
      // Keep local tasks state updated
      setTasks((prev) =>
        prev.map((t) =>
          t.id === selectedTask.id
            ? {
                ...t,
                title: editForm.title,
                description: editForm.description,
                priority: editForm.priority as any,
                expectedClosure: editForm.expectedClosure,
                updatedAt,
              }
            : t
        )
      );
      setSelectedTask(null);
      setIsEditingTask(false);
      toast({
        title: "Task updated",
        description: "Task was updated successfully",
      });
    } catch (err: any) {
      console.error("Failed to update task", err);
      toast({
        title: "Update failed",
        description: err?.response?.data?.detail || "Failed to update task",
        variant: "destructive",
      });
    }
  };

  const handleTaskMove = (taskId: string, newStatus: TaskStatus) => {
    const task = tasks.find((t) => t.id === taskId);
    if (!task) return;

    // Validate status change based on role
    const canChange = validateStatusChange(
      task.status,
      newStatus,
      currentRole,
      user?.id,
      task
    );

    if (!canChange.allowed) {
      toast({
        title: "Action Not Allowed",
        description: canChange.reason,
        variant: "destructive",
      });
      return;
    }

    // Map frontend status to backend status values
    const frontToBackStatus: Record<TaskStatus, string> = {
      todo: "to_do",
      inprogress: "in_progress",
      review: "review",
      done: "done",
    };

    (async () => {
      try {
        const backendRoleMap: { [k: string]: string } = {
          admin: "Admin",
          manager: "Manager",
          developer: "Developer",
        };
        const backendRole = backendRoleMap[currentRole] || "Developer";

        await taskService.updateTaskStatus(
          parseInt(task.id, 10),
          { status: frontToBackStatus[newStatus] as any },
          backendRole
        );

        // update local state on success
        const updatedAt = new Date().toISOString();
        setTasks((prev) =>
          prev.map((t) =>
            t.id === taskId ? { ...t, status: newStatus, updatedAt } : t
          )
        );

        toast({ title: "Task Moved", description: "Status updated" });
      } catch (err: any) {
        console.error("Failed to update task status", err);
        toast({
          title: "Update Failed",
          description:
            err?.response?.data?.detail || "Failed to update task status",
          variant: "destructive",
        });
      }
    })();
  };

  const handleStatusChange = (newStatus: TaskStatus) => {
    if (!selectedTask) return;
    // Status change validation based on role
    const canChange = validateStatusChange(
      selectedTask.status,
      newStatus,
      currentRole,
      user?.id,
      selectedTask
    );

    if (!canChange.allowed) {
      toast({
        title: "Action Not Allowed",
        description: canChange.reason,
        variant: "destructive",
      });
      return;
    }

    const frontToBackStatus: Record<TaskStatus, string> = {
      todo: "to_do",
      inprogress: "in_progress",
      review: "review",
      done: "done",
    };

    (async () => {
      try {
        const backendRoleMap: { [k: string]: string } = {
          admin: "Admin",
          manager: "Manager",
          developer: "Developer",
        };
        const backendRole = backendRoleMap[currentRole] || "Developer";

        await taskService.updateTaskStatus(
          parseInt(selectedTask.id, 10),
          { status: frontToBackStatus[newStatus] as any },
          backendRole
        );

        const updatedAt = new Date().toISOString();
        setTasks((prev) =>
          prev.map((t) =>
            t.id === selectedTask.id
              ? { ...t, status: newStatus, updatedAt }
              : t
          )
        );

        toast({
          title: "Status Updated",
          description: `Task ${
            selectedTask.id
          } moved to ${newStatus.toUpperCase()}`,
        });
        setSelectedTask(null);
      } catch (err: any) {
        console.error("Failed to patch task status", err);
        toast({
          title: "Update Failed",
          description:
            err?.response?.data?.detail || "Failed to update task status",
          variant: "destructive",
        });
      }
    })();
  };

  const validateStatusChange = (
    currentStatus: TaskStatus,
    newStatus: TaskStatus,
    role: string,
    userId?: string,
    task?: Task
  ): { allowed: boolean; reason?: string } => {
    // Developer: only allowed to move from In Progress -> Review
    if (role === "developer") {
      // Developers are allowed to move from To Do -> In Progress and In Progress -> Review
      if (
        (currentStatus === "inprogress" && newStatus === "review") ||
        (currentStatus === "todo" && newStatus === "inprogress")
      ) {
        return { allowed: true };
      }
      return {
        allowed: false,
        reason:
          "Developers can only move tasks from To Do -> In Progress or In Progress -> Review",
      };
    }

    // Manager: only the manager who created the task OR the reviewer can change
    // a task from Review -> Done OR Review -> In Progress
    if (role === "manager") {
      if (
        currentStatus === "review" &&
        (newStatus === "done" || newStatus === "inprogress")
      ) {
        if (!task || !userId) {
          return {
            allowed: false,
            reason: "Insufficient context to validate manager action",
          };
        }
        const isCreator = task.createdBy === userId;
        const isReviewer = task.reviewer === userId;
        if (isCreator || isReviewer) {
          return { allowed: true };
        }
        return {
          allowed: false,
          reason:
            "Only the manager who created the task or the reviewer can change status from Review",
        };
      }
      // Other manager transitions are not allowed by this rule
      return {
        allowed: false,
        reason:
          "Managers can only change Review -> Done or Review -> In Progress for their tasks",
      };
    }

    // Admin: allow any change
    return { allowed: true };
  };

  const priorityColors: Record<Priority, string> = {
    high: "bg-priority-high/10 text-priority-high",
    medium: "bg-priority-medium/10 text-priority-medium",
    low: "bg-priority-low/10 text-priority-low",
  };

  const statusColors: Record<TaskStatus, string> = {
    todo: "bg-status-todo/10 text-status-todo",
    inprogress: "bg-status-inprogress/10 text-status-inprogress",
    review: "bg-status-review/10 text-status-review",
    done: "bg-status-done/10 text-status-done",
  };

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Header */}
      <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold">My Tasks</h1>
          <p className="text-muted-foreground">Tasks assigned to you</p>
        </div>

        {/* Filters */}
        <div className="flex flex-col sm:flex-row gap-3">
          <div className="relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
            <Input
              placeholder="Search tasks..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-10 w-full sm:w-64"
            />
          </div>
          <Select
            value={priorityFilter}
            onValueChange={(value) =>
              setPriorityFilter(value as Priority | "all")
            }
          >
            <SelectTrigger className="w-full sm:w-40">
              <Filter className="h-4 w-4 mr-2" />
              <SelectValue placeholder="Priority" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">All Priorities</SelectItem>
              <SelectItem value="high">High</SelectItem>
              <SelectItem value="medium">Medium</SelectItem>
              <SelectItem value="low">Low</SelectItem>
            </SelectContent>
          </Select>
        </div>
      </div>

      <div className="flex gap-6">
        {/* Board */}
        <div className="flex-1">
          <KanbanBoard
            tasks={filteredTasks}
            onTaskClick={handleTaskClick}
            onTaskMove={handleTaskMove}
          />
        </div>
      </div>

      {/* Task Detail Dialog */}
      <Dialog open={!!selectedTask} onOpenChange={() => setSelectedTask(null)}>
        <DialogContent className="max-w-lg max-h-[80vh] overflow-y-auto">
          {selectedTask && (
            <>
              <DialogHeader>
                <div className="flex items-center gap-2 mb-2">
                  <Badge variant="outline" className="font-mono text-xs">
                    {selectedTask.id}
                  </Badge>
                  <Badge className={priorityColors[selectedTask.priority]}>
                    {selectedTask.priority}
                  </Badge>
                </div>
                <DialogTitle className="text-xl">
                  {selectedTask.title}
                </DialogTitle>
                <DialogDescription className="text-base">
                  {selectedTask.description}
                </DialogDescription>
              </DialogHeader>

              <div className="space-y-4 py-4">
                {/* Status */}
                <div className="flex items-center justify-between">
                  <span className="text-sm text-muted-foreground">Status</span>
                  <Badge className={statusColors[selectedTask.status]}>
                    {selectedTask.status.replace("inprogress", "In Progress")}
                  </Badge>
                </div>

                {/* Assignee */}
                <div className="flex items-center justify-between">
                  <span className="text-sm text-muted-foreground flex items-center gap-2">
                    <User className="h-4 w-4" /> Assigned To
                  </span>
                  <div className="text-sm font-medium text-right">
                    {selectedTask.assignedTo ? (
                      <div>
                        <div>
                          {employeeDetails[selectedTask.assignedTo]?.name ||
                            employeeNames[selectedTask.assignedTo] ||
                            "Loading..."}
                        </div>
                        <div className="text-xs text-muted-foreground">
                          {employeeDetails[selectedTask.assignedTo]
                            ?.designation && (
                            <span>
                              {
                                employeeDetails[selectedTask.assignedTo]
                                  ?.designation
                              }
                            </span>
                          )}
                          {employeeDetails[selectedTask.assignedTo]
                            ?.mgr_name && (
                            <span>{` • Reports to ${
                              employeeDetails[selectedTask.assignedTo]?.mgr_name
                            }`}</span>
                          )}
                        </div>
                      </div>
                    ) : (
                      "Unassigned"
                    )}
                  </div>
                </div>

                {/* Reviewer */}
                {selectedTask.reviewer && (
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-muted-foreground flex items-center gap-2">
                      <MessageSquare className="h-4 w-4" /> Reviewer
                    </span>
                    <div className="text-sm font-medium text-right">
                      <div>
                        {employeeDetails[selectedTask.reviewer]?.name ||
                          employeeNames[selectedTask.reviewer] ||
                          "Loading..."}
                      </div>
                      <div className="text-xs text-muted-foreground">
                        {employeeDetails[selectedTask.reviewer]
                          ?.designation && (
                          <span>
                            {
                              employeeDetails[selectedTask.reviewer]
                                ?.designation
                            }
                          </span>
                        )}
                        {employeeDetails[selectedTask.reviewer]?.mgr_name && (
                          <span>{` • Reports to ${
                            employeeDetails[selectedTask.reviewer]?.mgr_name
                          }`}</span>
                        )}
                      </div>
                    </div>
                  </div>
                )}

                {/* Due Date */}
                <div className="flex items-center justify-between">
                  <span className="text-sm text-muted-foreground flex items-center gap-2">
                    <Calendar className="h-4 w-4" /> Due Date
                  </span>
                  <span className="text-sm font-medium">
                    {format(
                      new Date(selectedTask.expectedClosure),
                      "MMM d, yyyy"
                    )}
                  </span>
                </div>

                {/* Updated At */}
                {selectedTask.updatedAt && (
                  <div className="flex items-center justify-between">
                    <span className="text-sm text-muted-foreground flex items-center gap-2">
                      <Clock className="h-4 w-4" /> Last Updated
                    </span>
                    <span className="text-sm">
                      {format(
                        new Date(selectedTask.updatedAt),
                        "MMM d, yyyy HH:mm"
                      )}
                    </span>
                  </div>
                )}
                {/* Remarks */}
                <div className="pt-4">
                  <h4 className="text-sm font-medium mb-2">Remarks</h4>
                  {loadingRemarks ? (
                    <p className="text-sm text-muted-foreground">
                      Loading remarks...
                    </p>
                  ) : remarks.length === 0 ? (
                    <p className="text-sm text-muted-foreground">
                      No remarks yet
                    </p>
                  ) : (
                    <div className="space-y-2 max-h-40 overflow-auto">
                      {remarks.map((r: any) => (
                        <div
                          key={r._id || r.id}
                          className="p-2 border rounded-md bg-muted/5"
                        >
                          <div className="text-sm">
                            {r.comment || r.content}
                          </div>
                          <div className="text-xs text-muted-foreground mt-1">
                            {r.created_at || r.createdAt}
                            {r.created_by
                              ? ` • by ${
                                  employeeNames[String(r.created_by)] ||
                                  r.created_by
                                }`
                              : ""}
                          </div>
                        </div>
                      ))}
                    </div>
                  )}

                  {isEditingTask && (
                    <div className="mt-3 space-y-2">
                      <textarea
                        className="w-full border rounded p-2 text-sm"
                        placeholder="Add a remark..."
                        value={newRemark}
                        onChange={(e) => setNewRemark(e.target.value)}
                      />
                      <input
                        type="file"
                        onChange={(e) =>
                          setRemarkFile(e.target.files?.[0] || null)
                        }
                      />
                      <div className="flex gap-2">
                        <Button
                          size="sm"
                          onClick={async () => {
                            if (!selectedTask) return;
                            if (!newRemark.trim()) {
                              toast({
                                title: "Validation",
                                description: "Remark cannot be empty",
                                variant: "destructive",
                              });
                              return;
                            }
                            try {
                              const backendRoleMap: { [k: string]: string } = {
                                admin: "Admin",
                                manager: "Manager",
                                developer: "Developer",
                              };
                              const backendRole =
                                backendRoleMap[currentRole] || "Developer";
                              await remarkService.createRemark(
                                {
                                  task_id: parseInt(selectedTask.id, 10),
                                  comment: newRemark,
                                },
                                backendRole,
                                remarkFile || undefined
                              );
                              // reload remarks
                              const r = await remarkService.getRemarksByTask(
                                parseInt(selectedTask.id, 10),
                                backendRole
                              );
                              setRemarks(r || []);
                              setNewRemark("");
                              setRemarkFile(null);
                              toast({
                                title: "Success",
                                description: "Remark added",
                              });
                            } catch (err: any) {
                              console.error("Failed to add remark", err);
                              toast({
                                title: "Error",
                                description:
                                  err?.response?.data?.detail ||
                                  "Failed to add remark",
                                variant: "destructive",
                              });
                            }
                          }}
                        >
                          Add Remark
                        </Button>
                        <Button
                          size="sm"
                          variant="outline"
                          onClick={() => {
                            setNewRemark("");
                            setRemarkFile(null);
                          }}
                        >
                          Cancel
                        </Button>
                      </div>
                    </div>
                  )}
                </div>
              </div>

              {/* Actions */}
              <div className="flex flex-wrap gap-2 pt-4 border-t">
                {/* Manager edit option: allow manager who created task to edit */}
                {currentRole === "manager" &&
                  selectedTask?.createdBy ===
                    String(parseInt(user?.id || "0", 10)) &&
                  !isEditingTask && (
                    <Button size="sm" variant="outline" onClick={startEdit}>
                      Edit Task
                    </Button>
                  )}
                {isEditingTask && (
                  <div className="w-full space-y-2">
                    <div>
                      <Input
                        value={editForm.title}
                        onChange={(e) =>
                          setEditForm((s) => ({ ...s, title: e.target.value }))
                        }
                      />
                    </div>
                    <div>
                      <Input
                        value={editForm.description}
                        onChange={(e) =>
                          setEditForm((s) => ({
                            ...s,
                            description: e.target.value,
                          }))
                        }
                      />
                    </div>
                    <div className="flex gap-2">
                      <Select
                        value={editForm.priority}
                        onValueChange={(v) =>
                          setEditForm((s) => ({ ...s, priority: v }))
                        }
                      >
                        <SelectTrigger className="w-40">
                          <SelectValue />
                        </SelectTrigger>
                        <SelectContent>
                          <SelectItem value="high">High</SelectItem>
                          <SelectItem value="medium">Medium</SelectItem>
                          <SelectItem value="low">Low</SelectItem>
                        </SelectContent>
                      </Select>
                      <Input
                        type="date"
                        value={
                          editForm.expectedClosure?.split("T")[0] ||
                          editForm.expectedClosure
                        }
                        onChange={(e) =>
                          setEditForm((s) => ({
                            ...s,
                            expectedClosure: e.target.value,
                          }))
                        }
                      />
                    </div>
                    <div className="flex gap-2">
                      <Button size="sm" onClick={saveEdit}>
                        Save
                      </Button>
                      <Button
                        size="sm"
                        variant="outline"
                        onClick={() => {
                          setIsEditingTask(false);
                        }}
                      >
                        Cancel
                      </Button>
                    </div>
                  </div>
                )}
                {selectedTask.status === "todo" && (
                  <Button
                    size="sm"
                    onClick={() => handleStatusChange("inprogress")}
                    className="bg-status-inprogress hover:bg-status-inprogress/90"
                  >
                    Start Progress
                  </Button>
                )}
                {selectedTask.status === "inprogress" && (
                  <Button
                    size="sm"
                    onClick={() => handleStatusChange("review")}
                    className="bg-status-review hover:bg-status-review/90"
                  >
                    Submit for Review
                  </Button>
                )}
                {selectedTask.status === "review" &&
                  currentRole !== "developer" && (
                    <>
                      <Button
                        size="sm"
                        onClick={() => handleStatusChange("done")}
                        className="bg-status-done hover:bg-status-done/90"
                      >
                        Approve & Complete
                      </Button>
                      <Button
                        size="sm"
                        variant="outline"
                        onClick={() => handleStatusChange("inprogress")}
                      >
                        Request Changes
                      </Button>
                    </>
                  )}
              </div>
            </>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
};

export default TaskBoard;
