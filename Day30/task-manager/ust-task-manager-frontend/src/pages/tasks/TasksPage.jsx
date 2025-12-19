import { useState, useEffect } from "react";
import { taskService } from "../../services/taskService";
import { useAuth } from "../../context/AuthContext";
import TaskModal from "../../components/tasks/TaskModal";
import TaskBoard from "../../components/tasks/TaskBoard";
import { toast } from "react-toastify";
import { LayoutList, Kanban, Plus, Search } from "lucide-react";

const TasksPage = () => {
  const { user } = useAuth();
  const [tasks, setTasks] = useState([]);
  const [viewMode, setViewMode] = useState(
    user && (user.role === "admin" || user.role === "manager")
      ? "board"
      : "table"
  ); // 'table' or 'board'
  const [viewAsEmployee, setViewAsEmployee] = useState(false); // Managers can toggle to view tasks assigned to them
  const [managerFilter, setManagerFilter] = useState("all"); // 'all' | 'created' | 'assigned' | 'reviewer'
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingTask, setEditingTask] = useState(null);
  const [searchTerm, setSearchTerm] = useState("");

  const fetchTasks = async () => {
    try {
      // For managers, prefer grouped endpoint when using filters or view-as-employee
      if (user?.role === "manager") {
        const myData = await taskService.getMy();
        // Default to all: combine unique tasks from the three groups
        const combined = [];
        const addUnique = (arr) => {
          arr.forEach((t) => {
            if (!combined.find((c) => c.task_id === t.task_id))
              combined.push(t);
          });
        };
        addUnique(myData.created || []);
        addUnique(myData.assigned || []);
        addUnique(myData.reviewer || []);

        setTasks(combined);
      } else {
        const data = await taskService.getAll();
        setTasks(data);
      }
    } catch (error) {
      toast.error("Failed to fetch tasks");
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  // If user loads after initial render, ensure admins/managers see board by default
  useEffect(() => {
    if (!user) return;
    if (user.role === "admin" || user.role === "manager") {
      setViewMode("board");
    }
  }, [user]);

  const handleCreateOrUpdate = async (data) => {
    try {
      if (editingTask) {
        await taskService.update(editingTask.task_id, data);
        toast.success("Task updated");
        // If a file was attached, upload it to the task
        if (data.file) {
          try {
            await taskService.uploadFile(editingTask.task_id, data.file);
            toast.success("File uploaded");
          } catch (err) {
            toast.error("Failed to upload file");
          }
        }
      } else {
        // If expected_closure not provided, default to today's date (YYYY-MM-DD)
        if (!data.expected_closure) {
          data.expected_closure = new Date().toISOString().split("T")[0];
        }
        // Validate: if manager assigns task to self, they cannot be the reviewer
        const assignedTo = Number(data.assigned_to);
        const reviewerId = Number(data.reviewer);
        if (
          user?.role === "manager" &&
          assignedTo === Number(user?.emp_id) &&
          reviewerId === Number(user?.emp_id)
        ) {
          toast.error(
            "You cannot set yourself as reviewer when assigning a task to yourself. Choose another reviewer."
          );
          return;
        }

        const resp = await taskService.create(data);
        // axios returns the response object; get created task id from resp.data
        const created = resp?.data || resp;
        const taskId =
          created?.task_id ||
          created?.taskId ||
          (created?.task && created.task.task_id);
        toast.success("Task created");

        if (data.file && taskId) {
          try {
            await taskService.uploadFile(taskId, data.file);
            toast.success("File uploaded");
          } catch (err) {
            toast.error("Failed to upload file");
          }
        }
      }
      setIsModalOpen(false);
      setEditingTask(null);
      fetchTasks();
    } catch (error) {
      toast.error("Operation failed");
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm("Are you sure?")) {
      await taskService.delete(id);
      fetchTasks();
      toast.success("Task deleted");
    }
  };

  const handleStatusChange = async (task, newStatus) => {
    try {
      // Optimistic Update (Update UI immediately)
      const updatedTasks = tasks.map((t) =>
        t.task_id === task.task_id ? { ...t, status: newStatus } : t
      );
      setTasks(updatedTasks);

      await taskService.updateStatus(task.task_id, newStatus, task.priority);
      toast.success("Status updated");
    } catch (e) {
      toast.error("Failed to update status");
      fetchTasks(); // Revert on error
    }
  };

  // Filter Logic
  let visibleTasks = tasks;
  if (user?.role === "manager") {
    if (viewAsEmployee) {
      // Quick toggle: assigned to manager
      visibleTasks = tasks.filter(
        (t) => Number(t.assigned_to) === Number(user.emp_id)
      );
    } else if (managerFilter && managerFilter !== "all") {
      if (managerFilter === "created") {
        visibleTasks = tasks.filter(
          (t) => Number(t.assigned_by) === Number(user.emp_id)
        );
      } else if (managerFilter === "assigned") {
        visibleTasks = tasks.filter(
          (t) => Number(t.assigned_to) === Number(user.emp_id)
        );
      } else if (managerFilter === "reviewer") {
        visibleTasks = tasks.filter(
          (t) => Number(t.reviewer) === Number(user.emp_id)
        );
      }
    }
  }

  const filteredTasks = visibleTasks.filter((t) =>
    t.title.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="p-6 h-[calc(100vh-64px)] flex flex-col">
      {/* Header Controls */}
      <div className="flex flex-col md:flex-row justify-between items-center mb-6 gap-4">
        {/* Left: Title & Search */}
        <div className="flex items-center gap-4 w-full md:w-auto">
          <h1 className="text-2xl font-bold text-gray-800">Tasks</h1>
          <div className="relative">
            <Search
              className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400"
              size={16}
            />
            <input
              type="text"
              placeholder="Search tasks..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="pl-9 pr-4 py-2 border rounded-full text-sm focus:ring-2 focus:ring-blue-500 w-64"
            />
          </div>
        </div>

        {/* Right: View Toggle & Create Button */}
        <div className="flex items-center gap-3">
          <div className="bg-white border rounded-lg p-1 flex items-center">
            <button
              onClick={() => setViewMode("table")}
              className={`p-2 rounded ${
                viewMode === "table"
                  ? "bg-blue-100 text-blue-600"
                  : "text-gray-500 hover:bg-gray-100"
              }`}
              title="Table View"
            >
              <LayoutList size={20} />
            </button>
            <button
              onClick={() => setViewMode("board")}
              className={`p-2 rounded ${
                viewMode === "board"
                  ? "bg-blue-100 text-blue-600"
                  : "text-gray-500 hover:bg-gray-100"
              }`}
              title="Board View"
            >
              <Kanban size={20} />
            </button>
          </div>

          {user.role !== "employee" && (
            <div className="flex items-center gap-2">
              {user.role === "manager" && (
                <button
                  onClick={() => setViewAsEmployee((v) => !v)}
                  className={`px-3 py-2 rounded ${
                    viewAsEmployee
                      ? "bg-green-600 text-white"
                      : "bg-gray-200 text-gray-700"
                  }`}
                  title="Switch view"
                >
                  {viewAsEmployee
                    ? "Switch to Manager View"
                    : "Switch to Employee View"}
                </button>
              )}
              {user.role === "manager" && (
                <select
                  value={managerFilter}
                  onChange={(e) => setManagerFilter(e.target.value)}
                  className="border rounded px-2 py-1 text-sm"
                  title="Manager Filter"
                >
                  <option value="all">All</option>
                  <option value="created">Created by me</option>
                  <option value="assigned">Assigned to me</option>
                  <option value="reviewer">Reviewer for me</option>
                </select>
              )}
              <button
                onClick={() => {
                  setEditingTask(null);
                  setIsModalOpen(true);
                }}
                className="bg-blue-600 text-white px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-blue-700 font-medium"
              >
                <Plus size={18} /> New Task
              </button>
            </div>
          )}
        </div>
      </div>

      {/* Content Area */}
      <div className="flex-1 overflow-auto">
        {viewMode === "table" ? (
          // TABLE VIEW
          <div className="bg-white shadow rounded-lg overflow-hidden border border-gray-200">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    ID
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    Title
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    Priority
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    Status
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    Assignee
                  </th>
                  <th className="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase">
                    Actions
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {filteredTasks.map((task) => (
                  <tr key={task.task_id} className="hover:bg-gray-50">
                    <td className="px-6 py-4 text-sm text-gray-500">
                      #{task.task_id}
                    </td>
                    <td className="px-6 py-4 text-sm font-medium text-gray-900">
                      {task.title}
                    </td>
                    <td className="px-6 py-4 text-sm">
                      <span
                        className={`px-2 py-1 rounded-full text-xs font-bold ${
                          task.priority === "high"
                            ? "bg-red-100 text-red-800"
                            : task.priority === "medium"
                            ? "bg-yellow-100 text-yellow-800"
                            : "bg-green-100 text-green-800"
                        }`}
                      >
                        {task.priority}
                      </span>
                    </td>
                    <td className="px-6 py-4 text-sm">
                      <span
                        className={`px-2 py-1 rounded-full text-xs font-semibold
                          ${
                            task.status === "COMPLETED"
                              ? "bg-green-100 text-green-700"
                              : task.status === "IN_PROGRESS"
                              ? "bg-blue-100 text-blue-700"
                              : task.status === "REVIEW"
                              ? "bg-orange-100 text-orange-700"
                              : "bg-gray-100 text-gray-700"
                          }`}
                      >
                        {task.status.replace("_", " ")}
                      </span>
                    </td>
                    <td className="px-6 py-4 text-sm text-gray-500">
                      {task.assigned_to}
                    </td>
                    <td className="px-6 py-4 text-right text-sm font-medium">
                      <button
                        onClick={() => {
                          setEditingTask(task);
                          setIsModalOpen(true);
                        }}
                        className="text-indigo-600 hover:text-indigo-900 mr-3"
                      >
                        Edit
                      </button>
                      {user.role !== "employee" && (
                        <button
                          onClick={() => handleDelete(task.task_id)}
                          className="text-red-600 hover:text-red-900"
                        >
                          Delete
                        </button>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          // BOARD VIEW
          <TaskBoard
            tasks={filteredTasks}
            onStatusChange={handleStatusChange}
            onTaskClick={(task) => {
              setEditingTask(task);
              setIsModalOpen(true);
            }}
          />
        )}
      </div>

      <TaskModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSubmit={handleCreateOrUpdate}
        initialData={editingTask}
        defaultAssigned={
          viewAsEmployee && user?.role === "manager" ? user?.emp_id : undefined
        }
      />
    </div>
  );
};

export default TasksPage;
