import React, { useEffect, useState } from "react";
import { getTasks, updateTask } from "../services/taskService";
import { FaArrowRight, FaCheckCircle, FaTimesCircle } from "react-icons/fa"; // Adding icons for actions
import { getAttachments, createAttachment, deleteAttachment, uploadAttachment } from "../services/attachmentService";
import api from "../services/api";
import { toast, ToastContainer } from "react-toastify";
import 'react-toastify/dist/ReactToastify.css';

const EmployeeTaskBoard = () => {
  const [tasks, setTasks] = useState([]);
  const [notifications, setNotifications] = useState([]);
  const [selectedTask, setSelectedTask] = useState(null);
  const [attachments, setAttachments] = useState([]);
  const [newFile, setNewFile] = useState(null);
  const [employeeRemark, setEmployeeRemark] = useState('');
  const [showReviewModal, setShowReviewModal] = useState(false);
  const empId = Number(localStorage.getItem('emp_id'));

  const loadTasks = async () => {
    const res = await getTasks();
    const all = res.data || [];
    // only show tasks assigned to this employee
    const mine = all.filter(t => Number(t.assigned_to) === Number(empId));
    setTasks(mine);

    // build simple notifications list based on recent updates
    const notes = mine
      .slice()
      .sort((a,b) => new Date(b.updated_at) - new Date(a.updated_at))
      .map(t => ({
        task_id: t.task_id,
        title: t.title,
        updated_at: t.updated_at,
        hasRemarks: Boolean(t.remarks),
      }));
    setNotifications(notes);
  };

  useEffect(() => {
    loadTasks();
  }, []);

  const loadAttachments = async (taskId) => {
    try {
      const res = await getAttachments();
      const taskAtt = (res || []).filter((a) => Number(a.task_id) === Number(taskId));
      setAttachments(taskAtt);
    } catch (err) {
      setAttachments([]);
    }
  };

  const updateStatus = async (task_id, currentStatus, newStatus) => {
    // Enforce employee rules on frontend too
    const allowed =
      (currentStatus === "TO_DO" && newStatus === "IN_PROGRESS") ||
      (currentStatus === "IN_PROGRESS" && newStatus === "REVIEW");

    if (!allowed) {
      alert(
        `As an employee you can only move TO_DO -> IN_PROGRESS or IN_PROGRESS -> REVIEW`
      );
      return;
    }

    // If sending to review, open modal to allow adding comments/attachments
    if (currentStatus === 'IN_PROGRESS' && newStatus === 'REVIEW') {
      const t = tasks.find(x => Number(x.task_id) === Number(task_id));
      setSelectedTask(t);
      setEmployeeRemark('');
      setNewFile(null);
      await loadAttachments(task_id);
      setShowReviewModal(true);
      return;
    }

    await updateTask(task_id, { status: newStatus });
    toast.success('Status updated');
    loadTasks();
  };

  const handleFilePick = (e) => {
    const f = e.target.files?.[0] || null;
    setNewFile(f);
  };

  const uploadFile = async (taskId) => {
    if (!newFile) {
      toast.error('Select a file first');
      return;
    }
    try {
      const form = new FormData();
      form.append('task_id', Number(taskId));
      form.append('uploaded_by', empId);
      form.append('file', newFile);

      await uploadAttachment(form);
      toast.success('Attachment uploaded');
      setNewFile(null);
      loadAttachments(taskId);
    } catch (err) {
      toast.error('Failed to upload');
    }
  };

  const sendToReviewConfirm = async () => {
    if (!selectedTask) return;
    try {
      const existing = selectedTask.remarks ? String(selectedTask.remarks) + '\n' : '';
      const appended = `${existing}Employee(${localStorage.getItem('user_name') || empId}): ${employeeRemark}`;
      await updateTask(selectedTask.task_id, { status: 'REVIEW', remarks: appended, updated_by: empId });
      // upload attachment metadata if any
      if (newFile) {
        const form = new FormData();
        form.append('task_id', selectedTask.task_id);
        form.append('uploaded_by', empId);
        form.append('file', newFile);
        await uploadAttachment(form);
      }
      toast.success('Sent to review');
      setShowReviewModal(false);
      setSelectedTask(null);
      setEmployeeRemark('');
      setNewFile(null);
      loadTasks();
    } catch (err) {
      toast.error('Failed to send to review');
    }
  };

  const downloadAttachment = async (id, fileName) => {
    try {
      const res = await api.get(`/attachments/${id}/download`, { responseType: 'blob' });
      const url = window.URL.createObjectURL(new Blob([res.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', fileName || 'file');
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);
    } catch (err) {
      console.error(err);
      toast.error('Failed to download file');
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-teal-100 to-blue-200 p-8">
  <div className="flex gap-6">
        {/* Left: Notifications + task list */}
        <div className="w-2/3">
          <h2 className="text-3xl font-semibold mb-4 text-gray-800">My Tasks</h2>

          <div className="mb-6">
            <h4 className="font-semibold mb-2">Recent notifications</h4>
            <div className="bg-white p-4 rounded shadow-sm">
              {notifications.length === 0 && <div className="text-sm text-gray-500">No recent notifications</div>}
              {notifications.map(n => (
                <div key={n.task_id} className="flex items-center justify-between p-2 border-b last:border-b-0">
                  <div>
                    <div className="text-sm font-medium">{n.title}</div>
                    <div className="text-xs text-gray-500">{n.hasRemarks ? 'New remark' : 'Updated'} • {n.updated_at ? new Date(n.updated_at).toLocaleString() : ''}</div>
                  </div>
                  <div>
                    <button onClick={() => { const t = tasks.find(x=>x.task_id===n.task_id); setSelectedTask(t); loadAttachments(n.task_id); }} className="text-sm text-blue-600 underline">View</button>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="overflow-x-auto bg-white rounded-lg shadow-xl p-4">
            <table className="w-full text-left text-gray-800">
              <thead>
                <tr className="bg-gradient-to-r from-teal-200 to-teal-300 text-gray-800">
                  <th className="p-4">Title</th>
                  <th className="p-4">Priority</th>
                  <th className="p-4">Status</th>
                  <th className="p-4">Actions</th>
                </tr>
              </thead>

              <tbody>
                {tasks.map((task) => (
                  <tr key={task.task_id} className="border-b border-gray-300 hover:bg-gradient-to-r from-teal-50 to-teal-100 transform transition-all duration-300">
                    <td className="p-4 cursor-pointer" onClick={() => { setSelectedTask(task); loadAttachments(task.task_id); }}>{task.title}</td>
                    <td className="p-4">
                      <span className={`font-semibold ${task.priority === "High" ? "text-red-600" : task.priority === "Medium" ? "text-yellow-500" : "text-green-500"}`}>{task.priority}</span>
                    </td>
                    <td className="p-4">{task.status}</td>

                    <td className="p-4 space-x-4">
                      {task.status === "TO_DO" && (
                        <button onClick={() => updateStatus(task.task_id, task.status, "IN_PROGRESS")} className="bg-gradient-to-r from-yellow-400 to-yellow-500 hover:bg-yellow-600 text-white px-4 py-2 rounded-full flex items-center justify-center transition-all duration-300 transform hover:scale-105"><FaArrowRight className="mr-2" /> Start</button>
                      )}

                      {task.status === "IN_PROGRESS" && (
                        <button onClick={() => updateStatus(task.task_id, task.status, "REVIEW")} className="bg-gradient-to-r from-blue-500 to-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-full flex items-center justify-center transition-all duration-300 transform hover:scale-105"><FaCheckCircle className="mr-2" /> Send to Review</button>
                      )}

                      {(task.status === "REVIEW" || task.status === "COMPLETED") && (
                        <span className="text-gray-500 text-sm flex items-center"><FaTimesCircle className="mr-2" />Waiting for manager review</span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Right: quick detail / placeholder */}
        <div className="w-1/3">
          <div className="bg-white p-4 rounded shadow-sm">
            <h4 className="font-semibold">Quick view</h4>
            <p className="text-sm text-gray-500 mt-2">Click a notification or task to view details, remarks and attachments. Use the Send to Review action to include a comment and attachment.</p>
          </div>
        </div>
      </div>

      {/* Task Details modal for employee */}
      {selectedTask && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-lg shadow-xl w-full max-w-4xl overflow-hidden">
            <div className="flex items-center justify-between p-4 border-b">
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 rounded-full bg-indigo-100 flex items-center justify-center text-indigo-700 font-bold">{(selectedTask.title || 'T').charAt(0)}</div>
                <div>
                  <h3 className="text-lg font-semibold">{selectedTask.title}</h3>
                  <div className="flex gap-2 items-center text-sm text-gray-600 mt-1">
                    <span className="px-2 py-1 rounded-full text-xs font-medium" style={{ backgroundColor: '#6CB3F4', color: '#fff' }}>{selectedTask.status}</span>
                    <span className="text-xs">Priority: <strong className="ml-1">{selectedTask.priority}</strong></span>
                    <span className="text-xs">Assigned to: <strong className="ml-1">{selectedTask.assigned_to}</strong></span>
                  </div>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <div className="text-sm text-gray-500">{selectedTask.created_at ? new Date(selectedTask.created_at).toLocaleString() : ''}</div>
                <button onClick={() => setSelectedTask(null)} className="text-gray-500 hover:bg-gray-100 p-2 rounded">Close</button>
              </div>
            </div>

            <div className="p-6 grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="md:col-span-2 space-y-4">
                <div>
                  <h4 className="font-semibold text-sm text-gray-700">Description</h4>
                  <p className="text-sm text-gray-800 mt-2">{selectedTask.description || 'No description provided.'}</p>
                </div>

                <div>
                  <h4 className="font-semibold text-sm text-gray-700">Conversation / Remarks</h4>
                  <div className="mt-3 space-y-2 max-h-64 overflow-auto pr-2">
                    {selectedTask.remarks ? (
                      String(selectedTask.remarks).split('\n').map((line, idx) => (
                        <div key={idx} className={`p-3 rounded-lg ${line.startsWith('Employee(') ? 'bg-blue-50 self-end' : 'bg-gray-100'}`}>
                          <div className="text-sm text-gray-800 whitespace-pre-wrap">{line}</div>
                        </div>
                      ))
                    ) : (
                      <div className="text-sm text-gray-500">No remarks yet.</div>
                    )}
                  </div>
                </div>

                {selectedTask.status === 'IN_PROGRESS' && (
                  <div className="mt-4">
                    <h4 className="font-semibold text-sm text-gray-700">Send to Review</h4>
                    <textarea value={employeeRemark} onChange={(e) => setEmployeeRemark(e.target.value)} rows={3} className="mt-2 w-full border rounded p-2" placeholder="Add a comment for the manager..." />
                    <div className="flex items-center gap-2 mt-2">
                      <input type="file" onChange={handleFilePick} accept=".pdf,.doc,.docx,.xls,.xlsx,.png,.jpg,.jpeg,.gif,.txt,.csv,.zip" />
                      <button onClick={() => uploadFile(selectedTask.task_id)} className="px-3 py-1 bg-green-600 text-white rounded">Upload</button>
                      <button onClick={sendToReviewConfirm} className="ml-auto px-4 py-2 bg-blue-600 text-white rounded">Send to Review</button>
                    </div>
                  </div>
                )}
              </div>

              <aside className="md:col-span-1">
                <div className="bg-gray-50 p-4 rounded">
                  <h5 className="font-semibold text-sm text-gray-700">Attachments</h5>
                  <div className="mt-3 space-y-2">
                    {attachments.length === 0 && <div className="text-sm text-gray-500">No attachments</div>}
                    {attachments.map((a) => (
                      <div key={a.id} className="flex items-center justify-between gap-3 bg-white p-2 rounded border">
                        <div className="flex items-center gap-3">
                          <div className="w-8 h-8 bg-gray-100 rounded flex items-center justify-center text-sm">{a.file_name.split('.').pop().toUpperCase()}</div>
                          <div className="text-sm">
                            <button onClick={(e) => { e.stopPropagation(); downloadAttachment(a.id, a.file_name); }} className="text-blue-600 underline bg-transparent border-0 p-0 m-0 cursor-pointer">{a.file_name}</button>
                            <div className="text-xs text-gray-500">{(a.file_size/1024).toFixed(1)} KB</div>
                          </div>
                        </div>
                        <div className="flex items-center gap-2">
                          <button className="text-xs text-red-500" onClick={() => { deleteAttachment(a.id); loadAttachments(selectedTask.task_id); }}>Delete</button>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </aside>
            </div>
          </div>
        </div>
      )}
      <ToastContainer position="top-right" autoClose={3000} hideProgressBar newestOnTop closeOnClick rtl={false} pauseOnFocusLoss draggable pauseOnHover />
    </div>
  );
};

export default EmployeeTaskBoard;
