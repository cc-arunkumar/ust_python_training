import React, { useState, useEffect } from "react";
import { Plus, AlertCircle, Users, Search } from "lucide-react";
import { useAuth } from "../../context/AuthContext";
import ApiService from "../../services/api";
import TaskModal from "./TaskModal";
import TaskDetailsModal from "./TaskDetailsModal";
import KanbanColumn from "./KanbanColumn";
import EmployeeModal from "../employees/EmployeeModal";
import DashboardCharts from "./DashboardCharts";
import { TASK_STATUSES } from "../../utils/constants";
import toast, { Toaster } from "react-hot-toast";
import { DragDropContext } from "@hello-pangea/dnd";

// Priority order for sorting
const PRIORITY_ORDER = { high: 3, medium: 2, low: 1 };

const KanbanBoard = ({ initialTasks, initialEmployees, onTasksChanged }) => {
  const { hasRole, activeRole } = useAuth();
  const canEdit = hasRole("ADMIN") || hasRole("MANAGER");

  const [tasks, setTasks] = useState(initialTasks ?? []);
  const [employees, setEmployees] = useState(initialEmployees ?? []);
  // compute progress for header display (based on current tasks list)
  const totalTasksCount = Array.isArray(tasks) ? tasks.length : 0;
  const completedTasksCount = Array.isArray(tasks)
    ? tasks.filter((t) => t.status === "DONE").length
    : 0;
  const progress =
    totalTasksCount === 0
      ? 0
      : Math.round((completedTasksCount / totalTasksCount) * 100);
  const [searchQuery, setSearchQuery] = useState("");
  // priorityFilter now acts as a sorting preference (which priority to surface first)
  const [priorityFilter, setPriorityFilter] = useState("ALL");
  const [showEmployeesModal, setShowEmployeesModal] = useState(false);
  const [showEmployeeEditor, setShowEmployeeEditor] = useState(false);
  const [editingEmployee, setEditingEmployee] = useState(null);
  const [selectedEmployeeId, setSelectedEmployeeId] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [selectedTask, setSelectedTask] = useState(null);
  const [editingTask, setEditingTask] = useState(null);
  const [showCreateModal, setShowCreateModal] = useState(false);
  const [sortOption, setSortOption] = useState("priority");

  useEffect(() => {
    if (initialTasks !== undefined) {
      setTasks(initialTasks);
      setLoading(false);
      setError("");
      // also set employees when provided
      if (initialEmployees !== undefined) setEmployees(initialEmployees);
      return;
    }

    fetchTasks();
    // if parent didn't provide employees, fetch them now
    if (initialEmployees === undefined) fetchEmployees();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [initialTasks, initialEmployees]);

  const fetchEmployees = async () => {
    try {
      const data = await ApiService.getEmployees();
      setEmployees(data);
    } catch (err) {
      // don't break the board if employees fail to load
      console.error("Failed to load employees", err);
      toast.error(err.message || "Failed to load employees");
    }
  };

  const fetchTasks = async (force = false) => {
    try {
      if (initialTasks !== undefined && !force) {
        setTasks(initialTasks);
        return;
      }

      const data = await ApiService.getTasks();
      setTasks(data);
    } catch (err) {
      setError(err.message);
      toast.error(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (taskId) => {
    try {
      await ApiService.deleteTask(taskId);
      toast.success("Task deleted successfully");
      // update local list immediately
      setTasks((prev) => prev.filter((t) => t.task_id !== taskId));
      // Ask parent (Layout) to refresh role-filtered data so stats update
      if (onTasksChanged) onTasksChanged();
      else await fetchTasks(true);
    } catch (err) {
      toast.error(err.message);
    }
  };

  /* =========================
     STATUS MOVEMENT RULES
     ========================= */
  const canMove = (from, to) => {
    const allowedTransitions = {
      TODO: ["ON_PROCESS"],
      ON_PROCESS: ["REVIEW"],
      REVIEW: ["ON_PROCESS", "DONE"],
      DONE: [],
    };

    return allowedTransitions[from]?.includes(to);
  };

  const onDragEnd = async (result) => {
    // Check if the user is an admin
    if (activeRole === "ADMIN") {
      toast.error("Admins cannot move tasks");
      return; // Prevent task movement
    }

    const { source, destination, draggableId } = result;

    if (!destination) return;
    if (source.droppableId === destination.droppableId) return;

    const fromStatus = source.droppableId;
    const toStatus = destination.droppableId;

    if (activeRole === "MANAGER") {
      // Managers can only move tasks from REVIEW to DONE or from REVIEW to ON_PROCESS
      if (
        fromStatus === "REVIEW" &&
        !["DONE", "ON_PROCESS"].includes(toStatus)
      ) {
        toast.error(
          "Managers can only move tasks from REVIEW to DONE or ON_PROCESS"
        );
        return;
      }
    }

    if (!canMove(fromStatus, toStatus)) {
      toast.error(`Cannot move task from ${fromStatus} to ${toStatus}`);
      return;
    }

    // Permission guard: developers are not allowed to move tasks from REVIEW -> DONE
    if (
      fromStatus === "REVIEW" &&
      toStatus === "DONE" &&
      activeRole === "DEVELOPER"
    ) {
      toast.error(
        "You don't have permission to move a task from Review to Done"
      );
      return;
    }

    try {
      await ApiService.updateTaskStatus(draggableId, toStatus);
      toast.success(`Task moved to ${toStatus.replace("_", " ")}`);
      // Update local task status to keep filtered view
      setTasks((prev) =>
        prev.map((t) =>
          t.task_id.toString() === draggableId.toString()
            ? { ...t, status: toStatus }
            : t
        )
      );
      if (onTasksChanged) onTasksChanged();
      else await fetchTasks(true);
    } catch {
      toast.error("Failed to update task");
    }
  };

  // Apply search / employee filters (priorityFilter no longer excludes tasks; it influences sorting)
  const filteredTasks = tasks.filter((t) => {
    // search filter (task title)
    if (searchQuery && searchQuery.trim() !== "") {
      const q = searchQuery.trim().toLowerCase();
      if (!t.title || !t.title.toLowerCase().includes(q)) return false;
    }

    // employee filter (assigned_to)
    if (selectedEmployeeId) {
      const assigned = t.assigned_to == null ? null : Number(t.assigned_to);
      if (assigned !== Number(selectedEmployeeId)) return false;
    }

    return true;
  });

  // Group tasks by status and apply sorting
  const groupedTasks = {};
  Object.values(TASK_STATUSES).forEach((status) => {
    groupedTasks[status] = filteredTasks
      .filter((t) => t.status === status)
      .sort((a, b) => {
        if (sortOption === "priority") {
          // If user selected a particular priority in the "Filter" select,
          // surface tasks with that priority first within each column.
          const selected =
            priorityFilter && priorityFilter !== "ALL"
              ? priorityFilter.toLowerCase()
              : null;

          if (selected) {
            const aIsSelected =
              a.priority && a.priority.toLowerCase() === selected;
            const bIsSelected =
              b.priority && b.priority.toLowerCase() === selected;
            if (aIsSelected && !bIsSelected) return -1;
            if (bIsSelected && !aIsSelected) return 1;
            // otherwise fall back to normal priority ordering
          }

          const aPriority = a.priority
            ? PRIORITY_ORDER[a.priority.toLowerCase()] || 0
            : 0;
          const bPriority = b.priority
            ? PRIORITY_ORDER[b.priority.toLowerCase()] || 0
            : 0;
          return bPriority - aPriority;
        } else {
          const aDate = a.expected_closure
            ? new Date(a.expected_closure)
            : new Date(0);
          const bDate = b.expected_closure
            ? new Date(b.expected_closure)
            : new Date(0);
          return aDate - bDate;
        }
      });
  });

  // Compute priority counts from filteredTasks
  const priorityCounts = { HIGH: 0, MEDIUM: 0, LOW: 0 };
  filteredTasks.forEach((t) => {
    const p = (t.priority || "").toString().toUpperCase();
    if (p === "HIGH") priorityCounts.HIGH += 1;
    else if (p === "MEDIUM") priorityCounts.MEDIUM += 1;
    else priorityCounts.LOW += 1;
  });

  // Compute status counts using groupedTasks
  const statusCounts = {};
  Object.values(TASK_STATUSES).forEach((s) => {
    statusCounts[s] = groupedTasks[s] ? groupedTasks[s].length : 0;
  });

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        Loading...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Toaster position="top-right" />

      {/* HEADER */}
      <div className="bg-white px-6 py-4 shadow-sm">
        <div className="max-w-7xl mx-auto flex items-center gap-4 flex-wrap">
          <h1 className="text-xl font-semibold flex-shrink-0">Task Board</h1>

          {/* Right-side controls grouped and responsive */}
          <div className="ml-auto flex items-center gap-3 flex-wrap">
            {/* Employee button */}
            <button
              onClick={() => setShowEmployeesModal(true)}
              className="flex items-center gap-2 px-3 py-2 rounded-lg bg-slate-100 text-sm hover:bg-slate-200 transition-colors"
            >
              <Users size={16} />
              <span className="hidden sm:inline">Employees</span>
            </button>

            {/* New Task button (visible only to editors) */}
            {canEdit && (
              <button
                onClick={() => setShowCreateModal(true)}
                className="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm flex items-center gap-2 hover:bg-blue-700 transition-colors"
              >
                <Plus size={16} />
                <span className=" xs:inline">New Task</span>
              </button>
            )}

            {/* Search + Filter grouped */}
            <div className="flex items-center gap-3">
              <div className="relative order-2 sm:order-1">
                <input
                  type="search"
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  placeholder="Search tasks by name..."
                  className="px-3 py-2 rounded-lg text-sm w-64 bg-white border border-slate-200 shadow-sm focus:outline-none focus:ring-1 focus:ring-blue-200"
                />
                <div className="absolute right-2 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none">
                  <Search size={14} />
                </div>
              </div>

              {/* Progress display */}
              <div className="flex items-center gap-2 mr-2">
                <div className="text-xs text-slate-500">Progress</div>
                <div className="w-32 bg-slate-100 rounded-full h-2 overflow-hidden">
                  <div
                    className="h-2 bg-blue-600 rounded-full transition-all duration-500"
                    style={{ width: `${progress}%` }}
                  />
                </div>
                <div className="text-xs text-slate-600 ml-2">{progress}%</div>
              </div>

              {/* Priority filter */}
              <select
                value={priorityFilter}
                onChange={(e) => setPriorityFilter(e.target.value)}
                className="bg-slate-100 rounded px-3 py-2 text-sm shadow-sm focus:outline-none"
                aria-label="Filter"
              >
                <option value="ALL">Filter</option>
                <option value="HIGH">High</option>
                <option value="MEDIUM">Medium</option>
                <option value="LOW">Low</option>
              </select>
            </div>
          </div>
        </div>
      </div>

      {/* ERROR */}
      {error && (
        <div className="m-6 bg-red-50 text-red-700 px-4 py-3 rounded-lg flex gap-2">
          <AlertCircle size={18} />
          {error}
        </div>
      )}

      {/* BOARD */}
      {/* Dashboard charts */}
      <div className="px-6">
        <div className="max-w-7xl mx-auto mt-6">
          <DashboardCharts
            priorityCounts={priorityCounts}
            statusCounts={statusCounts}
          />
        </div>
      </div>

      {/* BOARD */}
      <DragDropContext onDragEnd={onDragEnd}>
        <div className="p-6 flex gap-6 overflow-x-auto">
          {Object.entries(groupedTasks).map(([status, list]) => (
            <KanbanColumn
              key={status}
              status={status}
              tasks={list}
              employees={employees}
              onTaskView={setSelectedTask}
              onTaskEdit={canEdit ? setEditingTask : null}
              onTaskDelete={handleDelete}
            />
          ))}
        </div>
      </DragDropContext>

      {/* Employees modal */}
      {showEmployeesModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center px-4">
          <div
            className="absolute inset-0 bg-black/40"
            onClick={() => setShowEmployeesModal(false)}
          />
          <div className="relative bg-white rounded-lg p-6 shadow-lg w-full max-w-3xl z-10">
            <div className="flex justify-between items-center mb-4">
              <h4 className="text-lg font-semibold">Employees</h4>
              <div className="flex items-center gap-3">
                {hasRole("ADMIN") && (
                  <button
                    onClick={() => {
                      setEditingEmployee(null);
                      setShowEmployeeEditor(true);
                    }}
                    className="px-3 py-1 text-sm bg-blue-600 text-white rounded hover:bg-blue-700"
                  >
                    Add Employee
                  </button>
                )}
                <button
                  onClick={() => setShowEmployeesModal(false)}
                  className="text-slate-500"
                >
                  Close
                </button>
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 max-h-72 overflow-auto">
              {employees && employees.length > 0 ? (
                employees.map((emp) => (
                  <div
                    key={emp.emp_id}
                    className="p-3 bg-slate-50 rounded-md flex items-center justify-between shadow-sm"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 rounded-full bg-blue-500 text-white flex items-center justify-center font-semibold">
                        {emp.emp_name
                          ? emp.emp_name.charAt(0).toUpperCase()
                          : "-"}
                      </div>
                      <div>
                        <div className="font-medium truncate max-w-[12rem]">
                          {emp.emp_name}
                        </div>
                        <div className="text-xs text-slate-500">
                          ID: {emp.emp_id}
                        </div>
                      </div>
                    </div>
                    <div className="flex-shrink-0 flex items-center gap-2">
                      <button
                        onClick={() => {
                          setSelectedEmployeeId(emp.emp_id);
                          setShowEmployeesModal(false);
                        }}
                        className="px-3 py-1 text-sm bg-white border border-slate-200 rounded hover:bg-slate-50"
                      >
                        Filter
                      </button>

                      {hasRole("ADMIN") && (
                        <>
                          <button
                            onClick={() => {
                              setEditingEmployee(emp);
                              setShowEmployeeEditor(true);
                            }}
                            className="px-2 py-1 text-sm bg-white border border-slate-200 rounded hover:bg-slate-50"
                          >
                            Edit
                          </button>
                          <button
                            onClick={async () => {
                              if (!window.confirm(`Delete ${emp.emp_name}?`))
                                return;
                              try {
                                await ApiService.deleteEmployee(emp.emp_id);
                                toast.success("Employee deleted");
                                // refresh list
                                await fetchEmployees();
                              } catch (err) {
                                toast.error(err.message || "Failed to delete");
                              }
                            }}
                            className="px-2 py-1 text-sm bg-white border border-red-200 text-red-600 rounded hover:bg-red-50"
                          >
                            Delete
                          </button>
                        </>
                      )}
                    </div>
                  </div>
                ))
              ) : (
                <p className="text-sm text-slate-500">No employees available</p>
              )}
            </div>

            {selectedEmployeeId && (
              <div className="mt-4 text-right">
                <button
                  onClick={() => setSelectedEmployeeId(null)}
                  className="px-3 py-1 text-sm bg-red-50 text-red-600 rounded"
                >
                  Clear Employee Filter
                </button>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Employee Add/Edit Modal (reuses EmployeeModal) */}
      {showEmployeeEditor && (
        <EmployeeModal
          employee={editingEmployee}
          onClose={() => {
            setEditingEmployee(null);
            setShowEmployeeEditor(false);
          }}
          onSuccess={async () => {
            setShowEmployeeEditor(false);
            setEditingEmployee(null);
            await fetchEmployees();
          }}
        />
      )}

      {/* MODALS */}
      {selectedTask && (
        <TaskDetailsModal
          task={selectedTask}
          assignedEmployee={employees.find(
            (e) => Number(e.emp_id) === Number(selectedTask.assigned_to)
          )}
          onClose={() => setSelectedTask(null)}
          onUpdate={async () => {
            toast.success("Task updated successfully");
            if (onTasksChanged) onTasksChanged();
            else await fetchTasks(true);
          }}
        />
      )}

      {(editingTask || showCreateModal) && (
        <TaskModal
          task={editingTask}
          onClose={() => {
            setEditingTask(null);
            setShowCreateModal(false);
          }}
          onSuccess={async () => {
            setEditingTask(null);
            setShowCreateModal(false);
            // Let parent reload filtered lists (so stats update). If not provided, refresh locally.
            if (onTasksChanged) onTasksChanged();
            else await fetchTasks(true);
          }}
        />
      )}
    </div>
  );
};

export default KanbanBoard;
