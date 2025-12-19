import React, {
  createContext,
  useContext,
  useState,
  useCallback,
  useEffect,
} from "react";
import { Task, TaskStatus, Remark } from "@/types";
import api from "@/services/api";
import { toast } from "sonner";
import { CreateTaskInput } from "@/types";

/* -------------------- Context Type -------------------- */

interface TaskContextType {
  tasks: Task[];
  remarks: Remark[];
  updatingTasks: string[];
  updateTaskStatus: (
    taskId: string,
    newStatus: TaskStatus,
    updatedBy: string,
    remark?: string
  ) => void;
  reviewDecision: (
    taskId: string,
    action: "APPROVE" | "REJECT",
    remarks?: string,
    updatedBy?: string
  ) => void;
  updateTaskPriority: (
    taskId: string,
    priority: string,
    updatedBy: string
  ) => void;
  updateTaskExpectedClosure: (
    taskId: string,
    expectedClosure: string | null,
    updatedBy: string
  ) => void;
  updateTaskReviewer: (
    taskId: string,
    reviewer: string,
    updatedBy: string
  ) => void;
  createTask: (task: CreateTaskInput) => void;
  assignTask: (
    taskId: string,
    assignedTo: string,
    assignedBy: string,
    reviewer?: string
  ) => void;
  addRemark: (taskId: string, comment: string, createdBy: string) => void;
  loadRemarks: (taskId: string) => Promise<void>;
  deleteTask: (taskId: string) => void;
  getTaskById: (taskId: string) => Task | undefined;
}

const TaskContext = createContext<TaskContextType | undefined>(undefined);

/* -------------------- Provider -------------------- */

export const TaskProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [remarks, setRemarks] = useState<Remark[]>([]);
  const [updatingTasks, setUpdatingTasks] = useState<string[]>([]);

  /* -------------------- Fetch / Refresh Tasks -------------------- */
  const refreshTasks = useCallback(async () => {
    try {
      const res = await api.get("/api/tasks/");

      if (Array.isArray(res.data)) {
        const mapped: Task[] = res.data.map((t: any) => {
          return {
            t_id: t.t_id || `T${String(t.id).padStart(3, "0")}`,
            title: t.title,
            description: t.description,
            created_by:
              t.created_by ||
              (t.created_by_id
                ? `E${String(t.created_by_id).padStart(3, "0")}`
                : undefined),
            assigned_to:
              t.assigned_to ||
              (t.assigned_to_id
                ? `E${String(t.assigned_to_id).padStart(3, "0")}`
                : undefined),
            assigned_by:
              t.assigned_by ||
              (t.assigned_by_id
                ? `E${String(t.assigned_by_id).padStart(3, "0")}`
                : undefined),
            assigned_at: t.assigned_at,
            updated_at: t.updated_at,
            updated_by:
              t.updated_by ||
              (t.updated_by_id
                ? `E${String(t.updated_by_id).padStart(3, "0")}`
                : undefined),
            priority: t.priority || "medium",
            status: t.status || "TO_DO",
            reviewer: t.reviewer
              ? `E${String(t.reviewer).padStart(3, "0")}`
              : undefined,
            expected_closure: t.expected_closure,
            actual_closure: t.actual_closure,
          };
        });

        setTasks(mapped);
      }
    } catch (err) {
      console.error("Failed to fetch tasks", err);
      toast.error("Failed to load tasks");
    }
  }, []);

  useEffect(() => {
    let mounted = true;
    // initial load
    (async () => {
      if (!mounted) return;
      await refreshTasks();
    })();
    return () => {
      mounted = false;
    };
  }, [refreshTasks]);

  /* -------------------- Update Reviewer (Admin / Manager) -------------------- */
  const updateTaskReviewer = useCallback(
    (taskId: string, reviewer: string, updatedBy: string) => {
      (async () => {
        try {
          const stripDigits = (s?: string | number) => {
            if (s == null) return "";
            return String(s).replace(/\D/g, "");
          };

          const taskIdNum = Number(stripDigits(taskId));
          const reviewerId = Number(stripDigits(reviewer));
          if (!Number.isFinite(taskIdNum) || !Number.isFinite(reviewerId)) {
            toast.error("Invalid task id or reviewer id");
            return;
          }

          const payload: any = { reviewer_id: reviewerId };
          const res = await api.put(
            `/api/tasks/${taskIdNum}/reviewer`,
            payload
          );

          const updated = res.data;

          setTasks((prev) =>
            prev.map((task) =>
              task.t_id === taskId
                ? {
                    ...task,
                    reviewer: updated.reviewer
                      ? `E${String(updated.reviewer).padStart(3, "0")}`
                      : task.reviewer,
                    assigned_to: updated.assigned_to_id
                      ? `E${String(updated.assigned_to_id).padStart(3, "0")}`
                      : task.assigned_to,
                    assigned_at: updated.assigned_at || task.assigned_at,
                  }
                : task
            )
          );

          toast.success("Reviewer assigned");
        } catch (err: any) {
          console.error("Failed to assign reviewer", err);
          let msg = "Failed to assign reviewer";
          const data = err?.response?.data;
          if (data) {
            if (typeof data === "string") msg = data;
            else if (data?.detail) msg = String(data.detail);
            else if (data?.message) msg = String(data.message);
            else msg = JSON.stringify(data);
          } else if (err?.message) {
            msg = String(err.message);
          }
          toast.error(msg);
        }
      })();
    },
    []
  );

  /* -------------------- Update Status (UI only) -------------------- */

  const updateTaskStatus = useCallback(
    (
      taskId: string,
      newStatus: TaskStatus,
      updatedBy: string,
      remark?: string
    ) => {
      (async () => {
        try {
          // Call backend to change status — backend enforces DONE immutability
          const stripDigits = (s?: string | number) => {
            if (s == null) return "";
            return String(s).replace(/\D/g, "");
          };

          const taskIdNum = Number(stripDigits(taskId));
          if (!Number.isFinite(taskIdNum)) {
            toast.error("Invalid task id");
            return;
          }

          const payload: any = { status: newStatus };
          if (remark) payload.remark = remark;

          // If moving to REVIEW, prefer the dedicated send-to-review endpoint
          // which is guarded specifically for Employee role and contains
          // business logic for sending an IN_PROGRESS task to REVIEW.
          let res;
          if (newStatus === "REVIEW") {
            res = await api.patch(`/api/tasks/${taskIdNum}/send-to-review`);
          } else {
            res = await api.patch(`/api/tasks/${taskIdNum}`, payload);
          }

          const updated = res.data;

          setTasks((prev) =>
            prev.map((task) =>
              task.t_id === taskId
                ? {
                    ...task,
                    status: updated.status || newStatus,
                    updated_by: updated.updated_by
                      ? `E${String(updated.updated_by).padStart(3, "0")}`
                      : updatedBy,
                    updated_at: updated.updated_at || new Date().toISOString(),
                    ...(updated.status === "DONE"
                      ? {
                          actual_closure:
                            updated.actual_closure || new Date().toISOString(),
                        }
                      : {}),
                  }
                : task
            )
          );

          if (remark) {
            addRemark(taskId, remark, updatedBy);
          }

          toast.success(`Task moved to ${newStatus.replace("_", " ")}`);
        } catch (err: any) {
          // If backend reports validation / immutability, extract a string message
          console.error("Status update failed:", err);
          let msg = "Failed to update status";
          const data = err?.response?.data;
          if (data) {
            if (typeof data === "string") msg = data;
            else if (data?.detail) msg = String(data.detail);
            else if (data?.message) msg = String(data.message);
            else msg = JSON.stringify(data);
          } else if (err?.message) {
            msg = String(err.message);
          }

          toast.error(msg);
        }
      })();
    },
    []
  );

  /* -------------------- Update Priority -------------------- */
  const updateTaskPriority = useCallback(
    (taskId: string, priority: string, updatedBy: string) => {
      (async () => {
        try {
          const stripDigits = (s?: string | number) => {
            if (s == null) return "";
            return String(s).replace(/\D/g, "");
          };

          const taskIdNum = Number(stripDigits(taskId));
          if (!Number.isFinite(taskIdNum)) {
            toast.error("Invalid task id");
            return;
          }

          const payload = { priority };
          const res = await api.patch(
            `/api/tasks/${taskIdNum}/priority`,
            payload
          );

          const updated = res.data;

          setTasks((prev) =>
            prev.map((task) =>
              task.t_id === taskId
                ? {
                    ...task,
                    priority: updated.priority || priority,
                    updated_by: updated.updated_by || task.updated_by,
                    updated_at: updated.updated_at || new Date().toISOString(),
                  }
                : task
            )
          );

          toast.success("Priority updated");
        } catch (err: any) {
          console.error("Failed to update priority", err);
          let msg = "Failed to update priority";
          const data = err?.response?.data;
          if (data) {
            if (typeof data === "string") msg = data;
            else if (data?.detail) msg = String(data.detail);
            else if (data?.message) msg = String(data.message);
            else msg = JSON.stringify(data);
          } else if (err?.message) {
            msg = String(err.message);
          }
          toast.error(msg);
        }
      })();
    },
    []
  );

  /* -------------------- Update Expected Closure (Admin / Manager) -------------------- */
  const updateTaskExpectedClosure = useCallback(
    (taskId: string, expectedClosure: string | null, updatedBy: string) => {
      (async () => {
        try {
          const stripDigits = (s?: string | number) => {
            if (s == null) return "";
            return String(s).replace(/\D/g, "");
          };

          const taskIdNum = Number(stripDigits(taskId));
          if (!Number.isFinite(taskIdNum)) {
            toast.error("Invalid task id");
            return;
          }

          const payload: any = {
            expected_closure: expectedClosure
              ? new Date(expectedClosure).toISOString()
              : null,
          };

          const res = await api.patch(`/api/tasks/${taskIdNum}`, payload);
          const updated = res.data;

          setTasks((prev) =>
            prev.map((task) =>
              task.t_id === taskId
                ? {
                    ...task,
                    expected_closure:
                      updated.expected_closure ||
                      expectedClosure ||
                      task.expected_closure,
                    updated_by: updated.updated_by || task.updated_by,
                    updated_at: updated.updated_at || new Date().toISOString(),
                  }
                : task
            )
          );

          toast.success("Expected closure updated");
        } catch (err: any) {
          console.error("Failed to update expected closure", err);
          let msg = "Failed to update expected closure";
          const data = err?.response?.data;
          if (data) {
            if (typeof data === "string") msg = data;
            else if (data?.detail) msg = String(data.detail);
            else if (data?.message) msg = String(data.message);
            else msg = JSON.stringify(data);
          } else if (err?.message) {
            msg = String(err.message);
          }
          toast.error(msg);
        }
      })();
    },
    []
  );

  /* -------------------- Create Task (DB + UI) -------------------- */

  const createTask = useCallback((task: CreateTaskInput) => {
    (async () => {
      try {
        const payload = {
          title: task.title,
          description: task.description,
          priority: task.priority,
          expected_closure: task.expected_closure
            ? new Date(task.expected_closure).toISOString()
            : null,
        };

        const res = await api.post("/api/tasks/", payload);
        const created = res.data;

        const mapped: Task = {
          t_id: `T${String(created.id).padStart(3, "0")}`,
          title: created.title,
          description: created.description,
          created_by: created.created_by_id
            ? `E${String(created.created_by_id).padStart(3, "0")}`
            : undefined,
          assigned_to: created.assigned_to_id
            ? `E${String(created.assigned_to_id).padStart(3, "0")}`
            : undefined,
          assigned_by: created.assigned_by_id
            ? `E${String(created.assigned_by_id).padStart(3, "0")}`
            : undefined,
          assigned_at: created.assigned_at || new Date().toISOString(),
          updated_at: created.updated_at,
          updated_by: created.updated_by
            ? `E${String(created.updated_by).padStart(3, "0")}`
            : undefined,
          priority: created.priority || "medium",
          status: created.status || "TO_DO",
          reviewer: created.reviewer
            ? `E${String(created.reviewer).padStart(3, "0")}`
            : undefined,
          expected_closure: created.expected_closure,
          actual_closure: created.actual_closure,
        };

        setTasks((prev) => [...prev, mapped]);
        toast.success("Task created successfully");
      } catch (err) {
        console.error("Failed to create task", err);
        toast.error("Failed to create task");
      }
    })();
  }, []);

  /* -------------------- Assign Task (UI only) -------------------- */
  const assignTask = useCallback(
    async (
      taskId: string,
      assignedTo: string,
      assignedBy: string,
      reviewer?: string
    ) => {
      try {
        const stripDigits = (s?: string | number) => {
          if (s == null) return "";
          return String(s).replace(/\D/g, "");
        };

        const taskIdNum = Number(stripDigits(taskId)); // T002 → 2 or '2' -> 2
        const assignedToId = Number(stripDigits(assignedTo)); // E003 or '3' -> 3

        // Reject invalid or non-positive task ids — a value of 0 previously
        // resulted in calls to /api/tasks/0/assign which return 404.
        if (
          !Number.isFinite(taskIdNum) ||
          taskIdNum <= 0 ||
          !Number.isFinite(assignedToId) ||
          assignedToId <= 0
        ) {
          console.error("Invalid taskId or assignedToId", {
            taskId,
            assignedTo,
          });
          toast.error("Invalid assignee or task id");
          return;
        }

        const payload: any = { assigned_to_id: assignedToId };
        if (reviewer) {
          const reviewerId = Number(stripDigits(reviewer));
          if (Number.isFinite(reviewerId)) payload.reviewer = reviewerId;
        }

        const res = await api.put(`/api/tasks/${taskIdNum}/assign`, payload);

        const updatedTask = res.data;

        setTasks((prev) =>
          prev.map((task) =>
            task.t_id === taskId
              ? {
                  ...task,
                  assigned_to: updatedTask.assigned_to_id
                    ? `E${String(updatedTask.assigned_to_id).padStart(3, "0")}`
                    : task.assigned_to,
                  assigned_by: assignedBy
                    ? `E${String(Number(stripDigits(assignedBy))).padStart(
                        3,
                        "0"
                      )}`
                    : task.assigned_by,
                  assigned_at:
                    updatedTask.assigned_at || new Date().toISOString(),
                  status: updatedTask.status || task.status,
                }
              : task
          )
        );

        toast.success("Task assigned successfully");
      } catch (err: any) {
        // surface backend validation errors when possible
        if (err?.response?.data) {
          console.error("Assign error response:", err.response.data);
        } else {
          console.error("Failed to assign task", err);
        }
        toast.error("Failed to assign task");
      }
    },
    []
  );

  /* -------------------- Remarks -------------------- */

  /* -------------------- Review Decision (Manager / Reviewer) -------------------- */
  const reviewDecision = useCallback(
    (
      taskId: string,
      action: "APPROVE" | "REJECT",
      remarksText?: string,
      updatedBy?: string
    ) => {
      (async () => {
        try {
          const stripDigits = (s?: string | number) => {
            if (s == null) return "";
            return String(s).replace(/\D/g, "");
          };

          const taskIdNum = Number(stripDigits(taskId));
          if (!Number.isFinite(taskIdNum)) {
            toast.error("Invalid task id");
            return;
          }

          const payload: any = { action };
          if (remarksText) payload.remarks = remarksText;

          // mark as updating (optimistic UI)
          setUpdatingTasks((s) => Array.from(new Set([...s, taskId])));

          const res = await api.patch(
            `/api/tasks/${taskIdNum}/review-decision`,
            payload
          );

          const updated = res.data;

          setTasks((prev) =>
            prev.map((task) =>
              task.t_id === taskId
                ? {
                    ...task,
                    status:
                      updated.status ||
                      (action === "APPROVE" ? "DONE" : "IN_PROGRESS"),
                    reviewer: updated.reviewer
                      ? `E${String(updated.reviewer).padStart(3, "0")}`
                      : task.reviewer,
                    actual_closure:
                      updated.actual_closure || task.actual_closure,
                    updated_by: updated.updated_by
                      ? `E${String(updated.updated_by).padStart(3, "0")}`
                      : updatedBy || task.updated_by,
                    updated_at: updated.updated_at || new Date().toISOString(),
                  }
                : task
            )
          );

          if (remarksText) {
            // append remark locally (avoid depending on addRemark)
            const newRemark: Remark = {
              id: `R${String(remarks.length + 1).padStart(3, "0")}`,
              task_id: taskId,
              comment: remarksText,
              created_by: updatedBy || "",
              created_at: new Date().toISOString(),
            };
            setRemarks((prev) => [...prev, newRemark]);
          }

          // refresh tasks from server to ensure board reflects canonical state
          try {
            await refreshTasks();
          } catch (e) {
            // ignore refresh errors — we already optimistically updated local state
          }

          toast.success(`Review decision recorded: ${action}`);
        } catch (err: any) {
          console.error("Review decision failed:", err);
          let msg = "Failed to record review decision";
          const data = err?.response?.data;
          if (data) {
            if (typeof data === "string") msg = data;
            else if (data?.detail) msg = String(data.detail);
            else if (data?.message) msg = String(data.message);
            else msg = JSON.stringify(data);
          } else if (err?.message) {
            msg = String(err.message);
          }
          toast.error(msg);
        } finally {
          // clear updating flag
          setUpdatingTasks((s) => s.filter((id) => id !== taskId));
        }
      })();
    },
    [refreshTasks, remarks.length]
  );

  const addRemark = useCallback(
    (taskId: string, comment: string, createdBy: string) => {
      const newRemark: Remark = {
        id: `R${String(remarks.length + 1).padStart(3, "0")}`,
        task_id: taskId,
        comment,
        created_by: createdBy,
        created_at: new Date().toISOString(),
      };

      // optimistic local add
      setRemarks((prev) => [...prev, newRemark]);

      // persist to backend (best-effort)
      (async () => {
        try {
          const stripDigits = (s?: string | number) => {
            if (s == null) return "";
            return String(s).replace(/\D/g, "");
          };
          const taskIdNum = Number(stripDigits(taskId));
          if (!Number.isFinite(taskIdNum)) return;

          await api.post(`/api/tasks/${taskIdNum}/remarks`, { comment });
          // refresh remarks for this task
          await loadRemarks(taskId);
        } catch (err) {
          // ignore — we already have optimistic remark
          console.warn("Failed to persist remark", err);
        }
      })();
    },
    [remarks.length]
  );

  const loadRemarks = useCallback(async (taskId: string) => {
    try {
      const stripDigits = (s?: string | number) => {
        if (s == null) return "";
        return String(s).replace(/\D/g, "");
      };
      const taskIdNum = Number(stripDigits(taskId));
      if (!Number.isFinite(taskIdNum)) return;

      const res = await api.get(`/api/tasks/${taskIdNum}/remarks`);
      if (Array.isArray(res.data)) {
        // map server docs to Remark[] expected shape
        const mapped: Remark[] = res.data.map((d: any, idx: number) => ({
          id: d.id ? String(d.id) : `Rsrv${taskId}_${idx}`,
          // normalize task_id to the same prefixed format used in tasks (e.g. T012)
          task_id: d.task_id
            ? `T${String(d.task_id).padStart(3, "0")}`
            : String(taskId),
          comment: d.comment,
          created_by: d.created_by
            ? `E${String(d.created_by).padStart(3, "0")}`
            : "",
          created_at: d.created_at
            ? new Date(d.created_at).toISOString()
            : new Date().toISOString(),
        }));

        // replace remarks for this task
        setRemarks((prev) => {
          const others = prev.filter((r) => r.task_id !== taskId);
          return [...others, ...mapped];
        });
      }
    } catch (err) {
      console.warn("Failed to load remarks", err);
    }
  }, []);

  /* -------------------- Delete Task (UI only) -------------------- */

  const deleteTask = useCallback((taskId: string) => {
    setTasks((prev) => prev.filter((t) => t.t_id !== taskId));
    toast.success("Task deleted successfully");
  }, []);

  /* -------------------- Get Task -------------------- */

  const getTaskById = useCallback(
    (taskId: string) => tasks.find((t) => t.t_id === taskId),
    [tasks]
  );

  return (
    <TaskContext.Provider
      value={{
        tasks,
        remarks,
        updateTaskStatus,
        reviewDecision,
        updatingTasks,
        createTask,
        assignTask,
        updateTaskPriority,
        updateTaskExpectedClosure,
        updateTaskReviewer,
        addRemark,
        loadRemarks,
        deleteTask,
        getTaskById,
      }}
    >
      {children}
    </TaskContext.Provider>
  );
};

/* -------------------- Hook -------------------- */

export const useTasks = (): TaskContextType => {
  const context = useContext(TaskContext);
  if (!context) {
    throw new Error("useTasks must be used within a TaskProvider");
  }
  return context;
};
