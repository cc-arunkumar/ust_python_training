import React from "react";
import { remarkService } from "@/services/remarkService";
import { useAuth } from "@/context/AuthContext";

const Remarks: React.FC = () => {
  const [remarks, setRemarks] = React.useState<any[]>([]);
  const { user } = useAuth();

  React.useEffect(() => {
    const load = async () => {
      try {
        const res = await remarkService.getAllRemarks();
        setRemarks(res || []);
      } catch (e) {
        setRemarks([]);
      }
    };
    load();
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-semibold mb-4">Remarks Activity</h2>
      <div className="bg-card p-4 rounded-lg">
        {remarks.length === 0 && (
          <div className="text-muted-foreground p-4">No remarks found.</div>
        )}
        <ul className="space-y-3">
          {remarks.map((r: any) => (
            <li key={r._id} className="p-3 border rounded-md">
              <div className="flex items-center justify-between">
                <div className="text-sm font-medium">Task #{r.task_id}</div>
                <div className="text-xs text-muted-foreground">
                  {new Date(r.created_at).toLocaleString()}
                </div>
              </div>
              <div className="mt-2 text-sm">{r.comment}</div>
              {r.file_id && (
                <div className="mt-2">
                  <a
                    href={`/api/Remark/file?file_id=${encodeURIComponent(
                      r.file_id
                    )}`}
                    target="_blank"
                    rel="noreferrer"
                    className="text-sm text-primary underline"
                  >
                    {r.file_name || "Attachment"}
                  </a>
                </div>
              )}
              <div className="mt-2 text-xs text-muted-foreground">
                By: {r.created_by}
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Remarks;
