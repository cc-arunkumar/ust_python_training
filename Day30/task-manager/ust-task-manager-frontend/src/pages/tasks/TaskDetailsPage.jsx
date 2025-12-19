import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import api from "../../services/api";
import { toast } from "react-toastify";
import {
  ArrowLeft,
  Upload,
  FileText,
  Download,
  User,
  Calendar,
} from "lucide-react";
import { useAuth } from "../../context/AuthContext";

const TaskDetailsPage = () => {
  const { taskId } = useParams();
  const navigate = useNavigate();
  const [task, setTask] = useState(null);
  const [loading, setLoading] = useState(true);
  const [uploading, setUploading] = useState(false);

  // Fetch Task Details
  const fetchTask = async () => {
    try {
      const res = await api.get(`/api/tasks/${taskId}`);
      setTask(res.data);
    } catch (error) {
      console.error(error);
      toast.error("Task not found");
      navigate("/tasks");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTask();
  }, [taskId]);

  const { user } = useAuth();

  const STATUS_FLOW = ["TO_DO", "IN_PROGRESS", "REVIEW", "COMPLETED"];

  const canModifyStatus = () => {
    if (!user) return false;
    if (user.role === "admin" || user.role === "manager") return true;
    // Employee can modify only their own assigned tasks
    if (user.role === "employee")
      return task && task.assigned_to === user.emp_id;
    return false;
  };

  const changeStatus = async (newStatus) => {
    try {
      await api.patch(`/api/tasks/${taskId}/status`, {
        status: newStatus,
        priority: task.priority,
      });
      toast.success("Status updated");
      fetchTask();
    } catch (error) {
      console.error(error);
      toast.error("Failed to update status");
    }
  };

  // Handle File Upload
  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    setUploading(true);
    try {
      await api.post(`/api/tasks/${taskId}/files`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      toast.success("File uploaded successfully");
      fetchTask();
    } catch (error) {
      toast.error("Upload failed");
    } finally {
      setUploading(false);
    }
  };

  // Handle File Download
  const handleDownload = async (fileId, fileName) => {
    try {
      const response = await api.get(`/api/tasks/files/${fileId}`, {
        responseType: "blob",
      });

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", fileName);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      toast.error("Download failed");
    }
  };

  if (loading) return <div className="p-8 text-center">Loading...</div>;
  if (!task) return null;

  return (
    <div className="p-6 max-w-5xl mx-auto">
      <button
        onClick={() => navigate("/tasks")}
        className="flex items-center text-gray-600 hover:text-blue-600 mb-6 transition-colors"
      >
        <ArrowLeft size={20} className="mr-2" /> Back to Tasks
      </button>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 space-y-6">
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
            <div className="flex justify-between items-start mb-4">
              <span className="text-xs font-mono text-gray-400">
                #{task.task_id}
              </span>
              <span
                className={`px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider
                ${
                  task.priority === "high"
                    ? "bg-red-100 text-red-700"
                    : "bg-blue-100 text-blue-700"
                }`}
              >
                {task.priority}
              </span>
            </div>

            <h1 className="text-2xl font-bold text-gray-900 mb-4">
              {task.title}
            </h1>

            <div className="bg-gray-50 p-4 rounded-lg border border-gray-100 mb-6">
              <h3 className="text-sm font-bold text-gray-700 mb-2">
                Description / Remarks
              </h3>
              <p className="text-gray-600 whitespace-pre-wrap">
                {task.remarks || "No remarks provided."}
              </p>
            </div>

            <div className="grid grid-cols-2 gap-4 text-sm">
              <div className="flex items-center gap-3 text-gray-600">
                <User size={18} />
                <div>
                  <p className="text-xs text-gray-400">Assigned To</p>
                  <p className="font-medium">{task.assigned_to}</p>
                </div>
              </div>
              <div className="flex items-center gap-3 text-gray-600">
                <Calendar size={18} />
                <div>
                  <p className="text-xs text-gray-400">Due Date</p>
                  <p className="font-medium">
                    {task.expected_closure || "Not set"}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="space-y-6">
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
            <h3 className="font-bold text-gray-800 mb-4">Status</h3>
            <div
              className={`text-center p-3 rounded-lg font-bold mb-4
               ${
                 task.status === "COMPLETED"
                   ? "bg-green-100 text-green-700"
                   : task.status === "IN_PROGRESS"
                   ? "bg-blue-100 text-blue-700"
                   : "bg-yellow-100 text-yellow-700"
               }`}
            >
              {task.status.replace("_", " ")}
            </div>
            {/* Status controls: allow advance/revert along defined STATUS_FLOW */}
            {canModifyStatus() && task.status !== "COMPLETED" && (
              <div className="flex gap-2 justify-center">
                {(() => {
                  const idx = STATUS_FLOW.indexOf(task.status);
                  const prev = idx > 0 ? STATUS_FLOW[idx - 1] : null;
                  const next =
                    idx < STATUS_FLOW.length - 1 ? STATUS_FLOW[idx + 1] : null;
                  return (
                    <>
                      {prev && (
                        <button
                          onClick={() => changeStatus(prev)}
                          className="px-3 py-2 bg-gray-200 rounded text-sm hover:bg-gray-300"
                        >
                          Move to {prev.replace("_", " ")}
                        </button>
                      )}
                      {next && (
                        <button
                          onClick={() => changeStatus(next)}
                          className="px-3 py-2 bg-blue-600 text-white rounded text-sm hover:bg-blue-700"
                        >
                          Move to {next.replace("_", " ")}
                        </button>
                      )}
                    </>
                  );
                })()}
              </div>
            )}
          </div>

          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
            <h3 className="font-bold text-gray-800 mb-4 flex items-center gap-2">
              <FileText size={18} /> Attachments
            </h3>

            <div className="space-y-3 mb-6">
              {task.files && task.files.length > 0 ? (
                task.files.map((file) => (
                  <div
                    key={file.file_id}
                    className="flex justify-between items-center p-3 bg-gray-50 rounded-lg border hover:bg-gray-100 transition-colors"
                  >
                    <div className="flex items-center gap-2 overflow-hidden">
                      <FileText
                        size={16}
                        className="text-gray-400 flex-shrink-0"
                      />
                      <span
                        className="text-sm text-gray-700 truncate max-w-[120px]"
                        title={file.filename}
                      >
                        {file.filename}
                      </span>
                    </div>
                    <button
                      onClick={() =>
                        handleDownload(file.file_id, file.filename)
                      }
                      className="text-blue-600 hover:text-blue-800 p-1"
                      title="Download"
                    >
                      <Download size={16} />
                    </button>
                  </div>
                ))
              ) : (
                <p className="text-sm text-gray-400 italic text-center py-4">
                  No files attached
                </p>
              )}
            </div>

            <label
              className={`flex items-center justify-center w-full p-3 border-2 border-dashed border-blue-300 rounded-lg text-blue-600 font-medium cursor-pointer hover:bg-blue-50 transition-colors ${
                uploading ? "opacity-50 pointer-events-none" : ""
              }`}
            >
              <Upload size={18} className="mr-2" />
              {uploading ? "Uploading..." : "Upload File"}
              <input
                type="file"
                className="hidden"
                onChange={handleFileUpload}
              />
            </label>
          </div>
        </div>
      </div>
    </div>
  );
};

// 👇 THIS LINE IS CRITICAL. DO NOT FORGET IT!
export default TaskDetailsPage;
