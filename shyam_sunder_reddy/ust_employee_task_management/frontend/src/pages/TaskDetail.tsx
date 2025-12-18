import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { taskAPI, remarkAPI } from "../services/api";
import { ArrowLeft, MessageSquare, Plus, Upload } from "lucide-react";
import type { Task, Remark } from "../types";
import { format } from "date-fns";

const TaskDetail = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { activeRole, user } = useAuth();
  const [task, setTask] = useState<Task | null>(null);
  const [remarks, setRemarks] = useState<Remark[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [showRemarkModal, setShowRemarkModal] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      if (!id) return;

      // Build a list of roles to try: activeRole first, then any roles from the authenticated user
      const tried = new Set<string>();
      const rolesToTry: string[] = [];
      if (activeRole) {
        rolesToTry.push(activeRole);
        tried.add(activeRole);
      }
      if (user?.role && Array.isArray(user.role)) {
        user.role.forEach((r: string) => {
          if (r && !tried.has(r)) {
            rolesToTry.push(r);
            tried.add(r);
          }
        });
      }

      let lastError: any = null;
      for (const role of rolesToTry) {
        try {
          const [taskData, remarksData] = await Promise.all([
            taskAPI.getById(parseInt(id), role),
            remarkAPI.getByTask(parseInt(id), role).catch(() => []),
          ]);
          setTask(taskData);
          setRemarks(remarksData);
          lastError = null;
          break; // success
        } catch (err: any) {
          lastError = err;
          // If not an authorization error, stop and surface the problem
          const status = err?.response?.status;
          if (status && status !== 400 && status !== 403) {
            console.error("Error fetching task details:", err);
            break;
          }
          // otherwise try next role
        }
      }

      if (lastError) {
        console.error("Failed to fetch task with available roles:", lastError);
      }
      setIsLoading(false);
    };

    fetchData();
  }, [id, activeRole]);

  const handleStatusChange = async (newStatus: string) => {
    if (!id || !activeRole) return;

    try {
      await taskAPI.patchStatus(parseInt(id), newStatus, activeRole as string);
      setTask({ ...task!, status: newStatus });
    } catch (error) {
      console.error("Error updating status:", error);
      alert("Failed to update status");
    }
  };

  const handlePriorityChange = async (newPriority: string) => {
    if (!id || !activeRole) return;

    try {
      await taskAPI.patchPriority(
        parseInt(id),
        newPriority,
        activeRole as string
      );
      setTask({ ...task!, priority: newPriority as "high" | "medium" | "low" });
    } catch (error) {
      console.error("Error updating priority:", error);
      alert("Failed to update priority");
    }
  };

  const getStatusColor = (status?: string) => {
    switch (status) {
      case "DONE":
        return "bg-green-100 text-green-800 border-green-200";
      case "IN_PROGRESS":
        return "bg-yellow-100 text-yellow-800 border-yellow-200";
      case "REVIEW":
        return "bg-indigo-100 text-indigo-800 border-indigo-200";
      case "TO_DO":
        return "bg-orange-100 text-orange-800 border-orange-200";
      default:
        return "bg-gray-100 text-gray-800 border-gray-200";
    }
  };

  const getPriorityColor = (priority: string) => {
    switch (priority.toLowerCase()) {
      case "high":
        return "bg-red-100 text-red-800 border-red-200";
      case "medium":
        return "bg-yellow-100 text-yellow-800 border-yellow-200";
      case "low":
        return "bg-green-100 text-green-800 border-green-200";
      default:
        return "bg-gray-100 text-gray-800 border-gray-200";
    }
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-500"></div>
      </div>
    );
  }

  if (!task) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-500 mb-4">Task not found</p>
        <button onClick={() => navigate("/tasks")} className="btn-primary">
          Back to Tasks
        </button>
      </div>
    );
  }

  return (
    <div className="space-y-6 animate-fade-in">
      <button
        onClick={() => navigate("/tasks")}
        className="flex items-center gap-2 text-gray-600 hover:text-gray-800 transition-colors"
      >
        <ArrowLeft size={20} />
        Back to Tasks
      </button>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 space-y-6">
          <div className="card">
            <div className="flex items-start justify-between mb-4 min-w-0">
              <div className="flex-1 min-w-0">
                <h1 className="text-3xl font-bold text-gray-800 mb-2">
                  {task.title}
                </h1>
                <div className="flex flex-col items-start gap-2">
                  <span
                    className={`inline-flex items-center whitespace-nowrap px-3 py-1 rounded-lg text-sm font-medium border ${getStatusColor(
                      task.status
                    )}`}
                    style={{ maxWidth: "18rem" }}
                  >
                    {task.status || "TO_DO"}
                  </span>
                  <span
                    className={`inline-flex items-center whitespace-nowrap px-3 py-1 rounded-lg text-sm font-medium border ${getPriorityColor(
                      task.priority
                    )}`}
                    style={{ maxWidth: "10rem" }}
                  >
                    {task.priority}
                  </span>
                </div>
              </div>
            </div>

            <div className="mb-6">
              <h2 className="text-lg font-semibold text-gray-800 mb-2">
                Description
              </h2>
              <p className="text-gray-600 whitespace-pre-wrap">
                {task.description}
              </p>
            </div>

            <div className="grid grid-cols-2 gap-4 mb-6">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Status
                </label>
                <select
                  value={task.status || "TO_DO"}
                  onChange={(e) => handleStatusChange(e.target.value)}
                  className="input-field"
                >
                  <option value="TO_DO">To Do</option>
                  <option value="IN_PROGRESS">In Progress</option>
                  <option value="REVIEW">Review</option>
                  <option value="DONE">Done</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Priority
                </label>
                <select
                  value={task.priority}
                  onChange={(e) => handlePriorityChange(e.target.value)}
                  className="input-field"
                >
                  <option value="low">Low</option>
                  <option value="medium">Medium</option>
                  <option value="high">High</option>
                </select>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4 text-sm">
              <div>
                <span className="text-gray-600">Assigned To:</span>
                <span className="ml-2 font-medium text-gray-800">
                  {task.assigned_to || "Not assigned"}
                </span>
              </div>
              <div>
                <span className="text-gray-600">Reviewer:</span>
                <span className="ml-2 font-medium text-gray-800">
                  {task.reviewer || "Not assigned"}
                </span>
              </div>
              <div>
                <span className="text-gray-600">Expected Closure:</span>
                <span className="ml-2 font-medium text-gray-800">
                  {task.expected_closure
                    ? format(
                        new Date(task.expected_closure),
                        "MMM dd, yyyy HH:mm"
                      )
                    : "Not set"}
                </span>
              </div>
              <div>
                <span className="text-gray-600">Created:</span>
                <span className="ml-2 font-medium text-gray-800">
                  {task.assigned_at
                    ? format(new Date(task.assigned_at), "MMM dd, yyyy")
                    : "N/A"}
                </span>
              </div>
            </div>
          </div>

          <div className="card">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-xl font-semibold text-gray-800 flex items-center gap-2">
                <MessageSquare size={24} />
                Remarks
              </h2>
              <button
                onClick={() => setShowRemarkModal(true)}
                className="btn-primary flex items-center gap-2"
              >
                <Plus size={18} />
                Add Remark
              </button>
            </div>

            <div className="space-y-4">
              {remarks.length === 0 ? (
                <p className="text-gray-500 text-center py-8">No remarks yet</p>
              ) : (
                remarks.map((remark) => (
                  <div
                    key={remark._id}
                    className="p-4 border border-gray-200 rounded-lg bg-gray-50 animate-slide-up"
                  >
                    <div className="flex items-start justify-between mb-2">
                      <div>
                        <p className="font-medium text-gray-800">
                          Employee {remark.e_id}
                        </p>
                        <p className="text-xs text-gray-500">
                          {remark.created_at
                            ? format(
                                new Date(remark.created_at),
                                "MMM dd, yyyy HH:mm"
                              )
                            : "N/A"}
                        </p>
                      </div>
                    </div>
                    <p className="text-gray-700 mb-2">{remark.comment}</p>
                    {remark.file_url && (
                      <a
                        href={remark.file_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="text-primary-600 hover:text-primary-700 text-sm flex items-center gap-1"
                      >
                        <Upload size={16} />
                        View Attachment
                      </a>
                    )}
                  </div>
                ))
              )}
            </div>
          </div>
        </div>

        <div className="space-y-6">
          <div className="card">
            <h3 className="text-lg font-semibold text-gray-800 mb-4">
              Task Information
            </h3>
            <div className="space-y-3 text-sm">
              <div>
                <span className="text-gray-600">Task ID:</span>
                <span className="ml-2 font-medium text-gray-800">
                  {task.t_id}
                </span>
              </div>
              <div>
                <span className="text-gray-600">Assigned By:</span>
                <span className="ml-2 font-medium text-gray-800">
                  {task.assigned_by || "N/A"}
                </span>
              </div>
              <div>
                <span className="text-gray-600">Created By:</span>
                <span className="ml-2 font-medium text-gray-800">
                  {task.created_by || "N/A"}
                </span>
              </div>
              {task.updated_at && (
                <div>
                  <span className="text-gray-600">Last Updated:</span>
                  <span className="ml-2 font-medium text-gray-800">
                    {format(new Date(task.updated_at), "MMM dd, yyyy HH:mm")}
                  </span>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {showRemarkModal && (
        <RemarkModal
          taskId={parseInt(id!)}
          onClose={() => setShowRemarkModal(false)}
          onSuccess={() => {
            setShowRemarkModal(false);
            remarkAPI
              .getByTask(parseInt(id!), activeRole as string)
              .then(setRemarks);
          }}
        />
      )}
    </div>
  );
};

const RemarkModal: React.FC<{
  taskId: number;
  onClose: () => void;
  onSuccess: () => void;
}> = ({ taskId, onClose, onSuccess }) => {
  const { activeRole } = useAuth();
  const [comment, setComment] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!activeRole) return;

    setIsSubmitting(true);
    try {
      await remarkAPI.create(
        taskId,
        comment,
        activeRole as string,
        file || undefined
      );
      onSuccess();
    } catch (error) {
      console.error("Error creating remark:", error);
      alert("Failed to create remark");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4 animate-fade-in">
      <div className="bg-white rounded-xl shadow-xl max-w-lg w-full animate-scale-in">
        <div className="p-6 border-b border-gray-200">
          <h2 className="text-2xl font-bold text-gray-800">Add Remark</h2>
        </div>
        <form onSubmit={handleSubmit} className="p-6 space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Comment *
            </label>
            <textarea
              required
              value={comment}
              onChange={(e) => setComment(e.target.value)}
              className="input-field"
              rows={4}
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              Attachment
            </label>
            <input
              type="file"
              onChange={(e) => setFile(e.target.files?.[0] || null)}
              className="input-field"
            />
          </div>
          <div className="flex gap-3 pt-4">
            <button
              type="submit"
              className="btn-primary flex-1"
              disabled={isSubmitting}
            >
              {isSubmitting ? "Adding..." : "Add Remark"}
            </button>
            <button type="button" onClick={onClose} className="btn-secondary">
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default TaskDetail;
