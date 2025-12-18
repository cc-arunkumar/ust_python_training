import React, { useState } from "react";
import { Task } from "@/types";
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import api from "@/services/api";
import { useTasks } from "@/contexts/TaskContext";
import { useAuth } from "@/contexts/AuthContext";
import { toast } from "sonner";
import { Eye } from "lucide-react";

interface Props {
  task: Task;
  onClose: () => void;
}

const FileAttachmentModal: React.FC<Props> = ({ task, onClose }) => {
  const [remark, setRemark] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [uploadedInfo, setUploadedInfo] = useState<null | {
    file_id: string;
    filename: string;
  }>(null);
  const { addRemark } = useTasks();
  const { user } = useAuth();

  const stripDigits = (s?: string | number) => {
    if (s == null) return "";
    return String(s).replace(/\D/g, "");
  };

  const taskIdNum = Number(stripDigits(task.t_id));

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) setFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!remark.trim() && !file) {
      toast.error("Please add a remark or select a file to upload");
      return;
    }

    try {
      setUploading(true);

      let uploadedInfo = null as null | { file_id: string; filename: string };

      if (file) {
        const fd = new FormData();
        fd.append("file", file, file.name);
        const res = await api.post(`/api/tasks/${taskIdNum}/upload`, fd, {
          headers: { "Content-Type": "multipart/form-data" },
        });
        uploadedInfo = res.data;
        toast.success(`Uploaded ${uploadedInfo.filename}`);
        // store uploaded info so user can preview immediately
        setUploadedInfo(uploadedInfo);
      }

      // Compose remark text to include file reference when present
      let finalRemark = remark.trim();
      if (uploadedInfo) {
        const fname = uploadedInfo.filename || file?.name || "file";
        // embed file id so TaskDetailModal can render a preview button: [file:<file_id>:<filename>]
        finalRemark = `${finalRemark}${finalRemark ? "\n" : ""}[file:${
          uploadedInfo.file_id
        }:${fname}]`;
      }

      // Add remark locally (TaskContext currently keeps remarks in-memory)
      addRemark(task.t_id, finalRemark, user?.e_id || "");

      // If file was uploaded, keep modal open and allow user to preview it.
      // Clear remark and file selection but keep uploadedInfo available for preview.
      setRemark("");
      setFile(null);
      if (!uploadedInfo) {
        onClose();
      }
    } catch (err: any) {
      console.error("Upload failed", err);
      let msg = "Upload failed";
      if (err?.response?.data) msg = JSON.stringify(err.response.data);
      else if (err?.message) msg = err.message;
      toast.error(msg);
    } finally {
      setUploading(false);
    }
  };

  const viewUploadedFile = async (fileId: string) => {
    try {
      const res = await api.get(`/api/tasks/tasks/file/${fileId}`, {
        responseType: "blob",
      });
      const blob = new Blob([res.data], {
        type: res.headers["content-type"] || "application/octet-stream",
      });
      const url = URL.createObjectURL(blob);
      window.open(url, "_blank");
      // release object URL after some time
      setTimeout(() => URL.revokeObjectURL(url), 60_000);
    } catch (err: any) {
      console.error("Failed to fetch file", err);
      toast.error("Failed to fetch file");
    }
  };

  return (
    <Dialog open onOpenChange={onClose}>
      <DialogContent className="max-w-lg">
        <DialogHeader>
          <DialogTitle>Attach file / Add remark</DialogTitle>
        </DialogHeader>

        <div className="space-y-4 mt-2">
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-1">
              Remarks
            </label>
            <Textarea
              value={remark}
              onChange={(e) => setRemark(e.target.value)}
              placeholder="Add a short remark or description"
              className="min-h-[100px]"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-1">
              File / Photo
            </label>
            <input
              type="file"
              onChange={handleFileChange}
              accept="image/*,application/pdf"
            />
            {file && (
              <div className="text-sm mt-2 flex items-center gap-2">
                <span>Selected: {file.name}</span>
              </div>
            )}

            {uploadedInfo && (
              <div className="text-sm mt-2 flex items-center gap-2">
                <span className="font-medium">Uploaded:</span>
                <span>{uploadedInfo.filename}</span>
                <Button
                  size="sm"
                  variant="ghost"
                  onClick={() => viewUploadedFile(uploadedInfo.file_id)}
                  className="h-8 w-8 p-0"
                >
                  <Eye className="h-4 w-4" />
                </Button>
              </div>
            )}
          </div>

          <div className="flex gap-2 justify-end">
            <Button variant="outline" onClick={onClose} disabled={uploading}>
              Cancel
            </Button>
            <Button onClick={handleSubmit} disabled={uploading}>
              {uploading ? "Uploading..." : "Add Remark & Upload"}
            </Button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  );
};

export default FileAttachmentModal;
