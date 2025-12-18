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
  updateTaskStatus: (
    taskId: string,
    newStatus: TaskStatus,
    updatedBy: string,
    remark?: string
  ) => void;
  createTask: (task: CreateTaskInput) => void;
  assignTask: (
    taskId: string,
    assignedTo: string,
    assignedBy: string,
    reviewer?: string
  ) => void;
  addRemark: (taskId: string, comment: string, createdBy: string) => void;
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

  /* -------------------- Fetch Tasks -------------------- */

  useEffect(() => {
    let mounted = true;

    const fetchTasks = async () => {
      try {
        const res = await api.get("/api/tasks/");

        if (mounted && Array.isArray(res.data)) {
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
    };

    fetchTasks();
    return () => {
      mounted = false;
    };
  }, []);

  /* -------------------- Update Status (UI only) -------------------- */

  const updateTaskStatus = useCallback(
    (
      taskId: string,
      newStatus: TaskStatus,
      updatedBy: string,
      remark?: string
    ) => {
      setTasks((prev) =>
        prev.map((task) =>
          task.t_id === taskId
            ? {
                ...task,
                status: newStatus,
                updated_by: updatedBy,
                updated_at: new Date().toISOString(),
                ...(newStatus === "DONE"
                  ? { actual_closure: new Date().toISOString() }
                  : {}),
              }
            : task
        )
      );

      if (remark) {
        addRemark(taskId, remark, updatedBy);
      }

      toast.success(`Task moved to ${newStatus.replace("_", " ")}`);
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
    (
      taskId: string,
      assignedTo: string,
      assignedBy: string,
      reviewer?: string
    ) => {
      setTasks((prev) =>
        prev.map((task) =>
          task.t_id === taskId
            ? {
                ...task,
                assigned_to: assignedTo,
                assigned_by: assignedBy,
                assigned_at: new Date().toISOString(),
                reviewer: reviewer || task.reviewer,
              }
            : task
        )
      );

      toast.success("Task assigned successfully");
    },
    []
  );

  /* -------------------- Remarks -------------------- */

  const addRemark = useCallback(
    (taskId: string, comment: string, createdBy: string) => {
      const newRemark: Remark = {
        id: `R${String(remarks.length + 1).padStart(3, "0")}`,
        task_id: taskId,
        comment,
        created_by: createdBy,
        created_at: new Date().toISOString(),
      };

      setRemarks((prev) => [...prev, newRemark]);
    },
    [remarks.length]
  );

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
        createTask,
        assignTask,
        addRemark,
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
