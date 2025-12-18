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

interface Props {
  task: Task;
  onClose: () => void;
}

const FileAttachmentModal: React.FC<Props> = ({ task, onClose }) => {
  const [remark, setRemark] = useState("");
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
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
      }

      // Compose remark text to include file reference when present
      let finalRemark = remark.trim();
      if (uploadedInfo) {
        const fname = uploadedInfo.filename || file?.name || "file";
        finalRemark = `${finalRemark}${
          finalRemark ? "\n" : ""
        }[file attached: ${fname}]`;
      }

      // Add remark locally (TaskContext currently keeps remarks in-memory)
      addRemark(task.t_id, finalRemark, user?.e_id || "");

      setRemark("");
      setFile(null);
      onClose();
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
            {file && <div className="text-sm mt-2">Selected: {file.name}</div>}
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
