import React, { useState, useEffect } from "react";
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
import api from "@/services/api";
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
  Eye,
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
  const {
    updateTaskStatus,
    assignTask,
    addRemark,
    remarks,
    deleteTask,
    updateTaskPriority,
    updateTaskReviewer,
    updateTaskExpectedClosure,
    reviewDecision,
    loadRemarks,
  } = useTasks();
  const { user } = useAuth();
  const [newRemark, setNewRemark] = useState("");
  const [priorityVal, setPriorityVal] = useState<string>(
    task.priority || "medium"
  );
  // Normalize selected values to the raw employee id string (no prefix)
  const stripNonDigits = (s?: string | null) =>
    s ? String(s).replace(/\D/g, "") : "";

  const [selectedAssignee, setSelectedAssignee] = useState(
    stripNonDigits(task.assigned_to) || ""
  );
  const [selectedReviewer, setSelectedReviewer] = useState(
    stripNonDigits(task.reviewer) || ""
  );
  const formatToDateInput = (iso?: string | null) => {
    if (!iso) return "";
    try {
      return new Date(iso).toISOString().slice(0, 10);
    } catch {
      return "";
    }
  };
  const [expectedClosureVal, setExpectedClosureVal] = useState<string>(
    formatToDateInput(task.expected_closure)
  );

  useEffect(() => {
    setExpectedClosureVal(formatToDateInput(task.expected_closure));
  }, [task.expected_closure]);
  const { employees, getEmployeeById } = useEmployees();
  const [managersList, setManagersList] = useState<
    { emp_id: number | string | undefined; name: string; e_id: string }[]
  >([]);

  useEffect(() => {
    let mounted = true;
    (async () => {
      try {
        // use axios instance so Authorization header is included
        const res = await api.get("/api/users/managers");
        if (!mounted) return;
        const all = Array.isArray(res.data) ? res.data : [];
        setManagersList(
          all.map((u: any) => {
            const empId = u.emp_id != null ? u.emp_id : u.id;
            const empRec = getEmployeeById
              ? getEmployeeById(String(empId))
              : undefined;
            return {
              emp_id: empId,
              name:
                (empRec && empRec.name) ||
                u.name ||
                u.username ||
                u.email ||
                `User ${empId}`,
              e_id: empId ? `E${String(empId).padStart(3, "0")}` : u.e_id || "",
            };
          })
        );
      } catch (err) {
        // fallback silently — managers list will be empty and employees-based filter will still work
        console.warn("Failed to load users for managers list", err);
      }
    })();
    return () => {
      mounted = false;
    };
  }, []);

  const taskRemarks = remarks.filter((r) => r.task_id === task.t_id);

  useEffect(() => {
    // load persisted remarks for this task from backend when modal opens
    try {
      loadRemarks(task.t_id);
    } catch (e) {
      // ignore
    }
  }, [task.t_id]);
  // Resolve assignee/reviewer robustly: accept prefixed id (E001) or numeric id present on the task
  const resolveId = (val?: string | number) => {
    if (val == null) return undefined;
    const s = String(val);
    const digits = s.replace(/\D/g, "");
    return digits || undefined;
  };

  const assigneeId = task.assigned_to
    ? resolveId(task.assigned_to)
    : (resolveId((task as any).assigned_to_id) as string | undefined);
  const reviewerId = task.reviewer
    ? resolveId(task.reviewer)
    : (resolveId((task as any).reviewer) as string | undefined);

  const assignee = assigneeId ? getEmployeeById(assigneeId) : null;
  const reviewer = reviewerId ? getEmployeeById(reviewerId) : null;
  const creator = getEmployeeById(task.created_by);

  const isReviewer = task.reviewer === user?.e_id;
  // Disallow any status change when task is DONE
  // Only allow status change when:
  // - Employee: can move IN_PROGRESS -> REVIEW
  // - Reviewer (could be Manager or designated reviewer): can act on REVIEW
  const canChangeStatus =
    task.status !== "DONE" &&
    ((viewMode === "employee" && task.status === "IN_PROGRESS") ||
      (isReviewer && task.status === "REVIEW"));
  const canAssign = viewMode === "admin" || viewMode === "manager";
  const canEditMeta =
    (viewMode === "admin" || viewMode === "manager") && task.status !== "DONE";
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
    // For manager/reviewer actions on REVIEW tasks, use the review-decision
    // endpoint which records remarks and reviewer identity.
    if (
      task.status === "REVIEW" &&
      (newStatus === "IN_PROGRESS" || newStatus === "DONE") &&
      (isReviewer || viewMode === "manager")
    ) {
      // REJECT -> IN_PROGRESS, APPROVE -> DONE
      const action = newStatus === "DONE" ? "APPROVE" : "REJECT";
      // call reviewDecision from context
      try {
        reviewDecision(
          task.t_id,
          action,
          newRemark || undefined,
          user?.e_id || ""
        );
      } catch (e) {
        // fallback to generic update
        updateTaskStatus(
          task.t_id,
          newStatus,
          user?.e_id || "",
          newRemark || undefined
        );
      }
    } else {
      updateTaskStatus(
        task.t_id,
        newStatus,
        user?.e_id || "",
        newRemark || undefined
      );
    }
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
              <Flag className={`h-4 w-4 priority-${priorityVal}`} />
              <span className="text-muted-foreground">Priority:</span>
              {/* Allow only the task creator to change priority */}
              {user?.e_id === task.created_by ? (
                <div className="w-40">
                  <Select
                    value={priorityVal}
                    onValueChange={(value) => {
                      setPriorityVal(value);
                      updateTaskPriority(task.t_id, value, user?.e_id || "");
                    }}
                  >
                    <SelectTrigger>
                      <SelectValue className="capitalize">
                        {priorityVal}
                      </SelectValue>
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="low">Low</SelectItem>
                      <SelectItem value="medium">Medium</SelectItem>
                      <SelectItem value="high">High</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
              ) : (
                <span className="font-medium capitalize">{task.priority}</span>
              )}
            </div>
            <div className="flex items-center gap-2 text-sm">
              <Calendar className="h-4 w-4 text-muted-foreground" />
              <span className="text-muted-foreground">Due:</span>
              {canEditMeta ? (
                <input
                  type="date"
                  value={expectedClosureVal}
                  onChange={(e) => {
                    const v = e.target.value;
                    setExpectedClosureVal(v);
                    // null means clear the expected closure
                    updateTaskExpectedClosure(
                      task.t_id,
                      v || null,
                      user?.e_id || ""
                    );
                  }}
                  className="font-medium bg-transparent"
                />
              ) : (
                <span className="font-medium">
                  {task.expected_closure
                    ? format(new Date(task.expected_closure), "MMM d, yyyy")
                    : "Not set"}
                </span>
              )}
            </div>

            <div className="flex items-center gap-2 text-sm">
              <User className="h-4 w-4 text-muted-foreground" />
              <span className="text-muted-foreground">Assignee:</span>
              {canEditMeta && task.status !== "TO_DO" ? (
                <div className="w-40">
                  <Select
                    value={selectedAssignee}
                    onValueChange={(value) => {
                      setSelectedAssignee(value);
                      // call assignTask with current reviewer (if any) and logged-in user as assigned_by
                      assignTask(
                        task.t_id,
                        value,
                        user?.e_id || "",
                        selectedReviewer || undefined
                      );
                    }}
                  >
                    <SelectTrigger>
                      <SelectValue>
                        {selectedAssignee ? (
                          getEmployeeById(selectedAssignee)?.name || ""
                        ) : (
                          <span className="text-muted-foreground">
                            Select assignee
                          </span>
                        )}
                      </SelectValue>
                    </SelectTrigger>
                    <SelectContent>
                      {employees.map((emp) => (
                        <SelectItem key={emp.e_id} value={String(emp.e_id)}>
                          {emp.name}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>
              ) : (
                <span className="font-medium">
                  {assignee?.name || "Unassigned"}
                </span>
              )}
            </div>

            <div className="flex items-center gap-2 text-sm">
              <User className="h-4 w-4 text-muted-foreground" />
              <span className="text-muted-foreground">Reviewer:</span>
              {canEditMeta && task.status !== "TO_DO" ? (
                <div className="w-40">
                  <Select
                    value={selectedReviewer}
                    onValueChange={(value) => {
                      setSelectedReviewer(value);
                      updateTaskReviewer(task.t_id, value, user?.e_id || "");
                    }}
                  >
                    <SelectTrigger>
                      <SelectValue>
                        {selectedReviewer ? (
                          getEmployeeById(selectedReviewer)?.name || ""
                        ) : (
                          <span className="text-muted-foreground">
                            Select reviewer
                          </span>
                        )}
                      </SelectValue>
                    </SelectTrigger>
                    <SelectContent>
                      {(managersList.length > 0
                        ? managersList
                        : employees.filter((emp) => {
                            const desig = (emp.designation || "")
                              .toString()
                              .toLowerCase();
                            const hasRole = Array.isArray(emp.roles)
                              ? emp.roles.some(
                                  (r: any) =>
                                    String(r)
                                      .toLowerCase()
                                      .includes("manager") ||
                                    String(r).toLowerCase().includes("lead")
                                )
                              : false;
                            return (
                              desig.includes("manager") ||
                              desig.includes("lead") ||
                              hasRole
                            );
                          })
                      ).map((m: any) => (
                        <SelectItem
                          key={m.e_id || String(m.emp_id)}
                          value={m.e_id || String(m.emp_id)}
                        >
                          {m.name}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>
              ) : (
                <span className="font-medium">
                  {reviewer?.name || "Not set"}
                </span>
              )}
            </div>
          </div>

          {canAssign && task.status === "TO_DO" && (
            <div className="p-4 rounded-lg bg-muted/50 space-y-3">
              <h4 className="text-sm font-medium text-foreground">
                Assign Task
              </h4>
              <div className="grid grid-cols-2 gap-3">
                <div className="flex flex-col">
                  <span className="text-xs text-muted-foreground mb-1">
                    Select assignee
                  </span>
                  <Select
                    value={selectedAssignee}
                    onValueChange={(value) => {
                      // Immediately apply assignment when a different assignee is selected
                      setSelectedAssignee(value);
                      // call assignTask with current reviewer (if any) and logged-in user as assigned_by
                      assignTask(
                        task.t_id,
                        value,
                        user?.e_id || "",
                        selectedReviewer || undefined
                      );
                    }}
                  >
                    <SelectTrigger>
                      {/* Show the selected employee's name explicitly to avoid Radix rendering multiple concatenated values */}
                      <SelectValue>
                        {selectedAssignee ? (
                          getEmployeeById(selectedAssignee)?.name || ""
                        ) : (
                          <span className="text-black">Select assignee</span>
                        )}
                      </SelectValue>
                    </SelectTrigger>
                    <SelectContent>
                      {employees.map((emp) => (
                        <SelectItem key={emp.e_id} value={String(emp.e_id)}>
                          {emp.name}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>

                <div className="flex flex-col">
                  <span className="text-xs text-muted-foreground mb-1">
                    Select reviewer
                  </span>
                  <Select
                    value={selectedReviewer}
                    onValueChange={(value) => setSelectedReviewer(value)}
                  >
                    <SelectTrigger>
                      <SelectValue>
                        {selectedReviewer ? (
                          getEmployeeById(selectedReviewer)?.name || ""
                        ) : (
                          <span className="text-muted-foreground">
                            Select reviewer
                          </span>
                        )}
                      </SelectValue>
                    </SelectTrigger>
                    <SelectContent>
                      {(managersList.length > 0
                        ? managersList
                        : employees.filter((emp) => {
                            const desig = (emp.designation || "")
                              .toString()
                              .toLowerCase();
                            const hasRole = Array.isArray(emp.roles)
                              ? emp.roles.some(
                                  (r: any) =>
                                    String(r)
                                      .toLowerCase()
                                      .includes("manager") ||
                                    String(r).toLowerCase().includes("lead")
                                )
                              : false;
                            return (
                              desig.includes("manager") ||
                              desig.includes("lead") ||
                              hasRole
                            );
                          })
                      ).map((m: any) => (
                        <SelectItem
                          key={m.e_id || String(m.emp_id)}
                          value={m.e_id || String(m.emp_id)}
                        >
                          {m.name}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>
              </div>
              {/* Removed explicit 'Change' buttons — selecting a new assignee applies the change immediately. */}
              <Button
                onClick={handleAssign}
                disabled={!selectedAssignee}
                className="w-full"
              >
                Assign Task
              </Button>
            </div>
          )}

          {canAssign && task.status === "REVIEW" && (
            <div className="p-4 rounded-lg bg-muted/50 space-y-3">
              <h4 className="text-black font-medium text-foreground">
                Assign Reviewer
              </h4>
              <div className="w-72">
                <Select
                  value={selectedReviewer}
                  onValueChange={(value) => {
                    setSelectedReviewer(value);
                    // Allow Admin/Manager to assign reviewer for a REVIEW task
                    updateTaskReviewer(task.t_id, value, user?.e_id || "");
                  }}
                >
                  <SelectTrigger>
                    <SelectValue>
                      {selectedReviewer ? (
                        getEmployeeById(selectedReviewer)?.name || ""
                      ) : (
                        <span className="text-muted-foreground">
                          Select reviewer
                        </span>
                      )}
                    </SelectValue>
                  </SelectTrigger>
                  <SelectContent>
                    {(managersList.length > 0
                      ? managersList
                      : employees.filter((emp) => {
                          const desig = (emp.designation || "")
                            .toString()
                            .toLowerCase();
                          const hasRole = Array.isArray(emp.roles)
                            ? emp.roles.some(
                                (r: any) =>
                                  String(r).toLowerCase().includes("manager") ||
                                  String(r).toLowerCase().includes("lead")
                              )
                            : false;
                          return (
                            desig.includes("manager") ||
                            desig.includes("lead") ||
                            hasRole
                          );
                        })
                    ).map((m: any) => (
                      <SelectItem
                        key={m.e_id || String(m.emp_id)}
                        value={m.e_id || String(m.emp_id)}
                      >
                        {m.name}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>
            </div>
          )}

          {canChangeStatus && (
            <div className="p-4 rounded-lg bg-muted/50 space-y-3">
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
                // detect embedded file marker in remark.comment of form: [file:<file_id>:<filename>]
                const fileMatch = remark.comment.match(
                  /\[file:([^:\]]+):([^\]]+)\]/
                );
                const fileId = fileMatch ? fileMatch[1] : null;
                const fileName = fileMatch ? fileMatch[2] : null;

                // remove marker from displayed text
                const displayComment = remark.comment
                  .replace(fileMatch?.[0] ?? "", "")
                  .trim();

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

                    <div className="flex items-start justify-between gap-4">
                      <p className="text-muted-foreground flex-1">
                        {displayComment ||
                          (fileName ? `Attached: ${fileName}` : "")}
                      </p>

                      {fileId && (
                        <div className="ml-2">
                          <Button
                            size="sm"
                            variant="ghost"
                            onClick={async () => {
                              try {
                                const res = await api.get(
                                  `/api/tasks/tasks/file/${fileId}`,
                                  {
                                    responseType: "blob",
                                  }
                                );
                                const blob = new Blob([res.data], {
                                  type:
                                    res.headers["content-type"] ||
                                    "application/octet-stream",
                                });
                                const url = URL.createObjectURL(blob);
                                window.open(url, "_blank");
                                setTimeout(
                                  () => URL.revokeObjectURL(url),
                                  60_000
                                );
                              } catch (err) {
                                console.error("Failed to fetch file", err);
                                // best-effort toast if sonner is available
                                try {
                                  (window as any).toast?.error?.(
                                    "Failed to fetch file"
                                  );
                                } catch {}
                              }
                            }}
                            className="h-8 w-8 p-0"
                          >
                            <Eye className="h-4 w-4" />
                          </Button>
                        </div>
                      )}
                    </div>
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
