import { useEffect, useState } from "react";
import toast from "react-hot-toast";
import {
  uploadTaskFile,
  getTaskFiles,
  downloadTaskFile,
} from "../api/taskFiles.api";

export default function TaskFilesModal({ task, onClose }) {
  const [files, setFiles] = useState([]);
  const [uploading, setUploading] = useState(false);

  const loadFiles = async () => {
    const res = await getTaskFiles(task.t_id);
    setFiles(res.data);
  };

  useEffect(() => {
    loadFiles();
  }, []);

  const handleUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    try {
      setUploading(true);
      await uploadTaskFile(task.t_id, file);
      toast.success("File uploaded");
      loadFiles();
    } catch {
      toast.error("Upload failed");
    } finally {
      setUploading(false);
    }
  };

  const handleDownload = async (fileId, filename) => {
    const res = await downloadTaskFile(task.t_id, fileId);

    const blob = new Blob([res.data]);
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    a.click();
    window.URL.revokeObjectURL(url);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      <div className="absolute inset-0 bg-black/40" onClick={onClose} />

      <div className="relative bg-white w-full max-w-md rounded-lg shadow p-5">
        <h2 className="text-lg font-semibold mb-4">
          Attachments — TASK-{task.t_id}
        </h2>

        {/* Upload */}
        <label className="block mb-3">
          <input
            type="file"
            onChange={handleUpload}
            disabled={uploading}
            className="hidden"
          />
          <span className="cursor-pointer inline-block bg-blue-600 text-white px-4 py-2 rounded text-sm">
            {uploading ? "Uploading..." : "Upload File"}
          </span>
        </label>

        {/* File list */}
        <div className="space-y-2 max-h-60 overflow-y-auto">
          {files.length === 0 && (
            <p className="text-sm text-gray-500">No files uploaded</p>
          )}

          {files.map((f) => (
            <div
              key={f.file_id}
              className="flex justify-between items-center border rounded px-3 py-2 text-sm"
            >
              <span className="truncate">{f.filename}</span>
              <button
                onClick={() =>
                  handleDownload(f.file_id, f.filename)
                }
                className="text-blue-600 hover:underline"
              >
                Download
              </button>
            </div>
          ))}
        </div>

        <div className="mt-4 text-right">
          <button
            onClick={onClose}
            className="text-sm px-3 py-1 bg-gray-100 rounded"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}
