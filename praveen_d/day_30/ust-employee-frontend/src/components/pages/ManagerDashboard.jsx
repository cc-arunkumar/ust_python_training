import { useState, useEffect } from 'react';
import { Users, LogOut, Plus, FolderKanban } from 'lucide-react';  // Icons for header/button
import { api } from '../../services/api';  // Import API for createTask

const ManagerDashboard = ({
  user,
  tasks,
  token,
  onLogout,
  onSwitchRole,
  error,
  onError,
  onUpdateTasks,
  onCreateTask,
}) => {
  const [activeTab, setActiveTab] = useState('tasks');  // If you add tabs later
  const [showCreateTask, setShowCreateTask] = useState(false);
  const [taskForm, setTaskForm] = useState({
    task_id: '',
    name: '',
    description: '',
    assigned_to: '',
    priority: 'MEDIUM',
    expected_closure: '',
  });
  const [dashboardLoading, setDashboardLoading] = useState(true);
  const [localLoading, setLocalLoading] = useState(false);  // For form actions

  const handleCreateTask = async (e) => {
    e.preventDefault();
    setLocalLoading(true);
    try {
      const newTask = {
        ...taskForm,
        status: 'TO_DO',
        assigned_by: user?.emp_id,
        created_by: user?.emp_id,
        // reviewer optional
      };
      const created = await api.createTask(newTask, token);
      onCreateTask(created);  // Update parent state
      setShowCreateTask(false);
      setTaskForm({
        task_id: '',
        name: '',
        description: '',
        assigned_to: '',
        priority: 'MEDIUM',
        expected_closure: '',
      });
    } catch (err) {
      onError(err.message);
    } finally {
      setLocalLoading(false);
    }
  };

  // Optional: Handle task updates if needed (e.g., for review)
  const handleUpdateTask = async (taskId, updates) => {
    try {
      const updated = await api.updateTaskStatus(taskId, updates.status_, updates.remarks || '', token);
      onUpdateTasks(updated);
    } catch (err) {
      onError(err.message);
    }
  };

  useEffect(() => {
    // Set loading false once tasks are available (fetched in App)
    if (tasks.length >= 0) {
      setDashboardLoading(false);
    }
  }, [tasks]);

  if (dashboardLoading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-lg">Loading...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white border-b border-gray-200 sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-3">
              <Users className="w-8 h-8 text-green-600" />
              <div>
                <h1 className="text-2xl font-bold text-gray-900">Manager Dashboard</h1>
                <p className="text-sm text-gray-600">{user?.name}</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              {user?.role === 'ADMIN' && (
                <button
                  onClick={onSwitchRole}
                  className="text-gray-600 hover:text-gray-900"
                >
                  Switch Role
                </button>
              )}
              <button
                onClick={onLogout}
                className="flex items-center space-x-2 text-gray-600 hover:text-gray-900"
              >
                <LogOut className="w-5 h-5" />
                <span>Logout</span>
              </button>
            </div>
          </div>
        </div>
      </header>
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {error && (
          <div className="bg-red-50 text-red-600 px-4 py-3 rounded-lg text-sm mb-4">{error}</div>
        )}
        <div className="mb-6">
          <button
            onClick={() => setShowCreateTask(true)}
            disabled={localLoading}
            className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 flex items-center space-x-2 disabled:opacity-50"
          >
            <Plus className="w-5 h-5" />
            <span>Create New Task</span>
          </button>
        </div>

        {/* Create Task Modal */}
        {showCreateTask && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg max-w-2xl w-full p-6">
              <h3 className="text-xl font-bold mb-4">Create New Task</h3>
              <form onSubmit={handleCreateTask} className="space-y-4">
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Task ID</label>
                    <input
                      type="text"
                      value={taskForm.task_id}
                      onChange={(e) => setTaskForm({ ...taskForm, task_id: e.target.value })}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                      disabled={localLoading}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Priority</label>
                    <select
                      value={taskForm.priority}
                      onChange={(e) => setTaskForm({ ...taskForm, priority: e.target.value })}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      disabled={localLoading}
                    >
                      <option value="HIGH">High</option>
                      <option value="MEDIUM">Medium</option>
                      <option value="LOW">Low</option>
                    </select>
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Task Name</label>
                  <input
                    type="text"
                    value={taskForm.name}
                    onChange={(e) => setTaskForm({ ...taskForm, name: e.target.value })}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                    required
                    disabled={localLoading}
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">Description</label>
                  <textarea
                    value={taskForm.description}
                    onChange={(e) => setTaskForm({ ...taskForm, description: e.target.value })}
                    className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                    rows="3"
                    required
                    disabled={localLoading}
                  />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Assign To (Employee ID)</label>
                    <input
                      type="text"
                      value={taskForm.assigned_to}
                      onChange={(e) => setTaskForm({ ...taskForm, assigned_to: e.target.value })}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                      disabled={localLoading}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Expected Closure</label>
                    <input
                      type="date"
                      value={taskForm.expected_closure}
                      onChange={(e) => setTaskForm({ ...taskForm, expected_closure: e.target.value })}
                      className="w-full px-3 py-2 border border-gray-300 rounded-lg"
                      required
                      disabled={localLoading}
                    />
                  </div>
                </div>
                <div className="flex justify-end space-x-3 pt-4">
                  <button
                    type="button"
                    onClick={() => setShowCreateTask(false)}
                    className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 disabled:opacity-50"
                    disabled={localLoading}
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    disabled={localLoading}
                    className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50"
                  >
                    {localLoading ? 'Creating...' : 'Create Task'}
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}

        {/* Tasks Table */}
        <div className="bg-white rounded-lg shadow overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead className="bg-gray-50 border-b border-gray-200">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Task</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Assigned To</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Status</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Priority</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Due Date</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-200">
                {tasks.map((task) => (
                  <tr key={task.task_id} className="hover:bg-gray-50">
                    <td className="px-6 py-4">
                      <div className="flex items-center space-x-3">
                        <FolderKanban className="w-4 h-4 text-gray-400" />  {/* Simple icon */}
                        <div>
                          <div className="font-medium text-gray-900">{task.name}</div>
                          <div className="text-sm text-gray-500">{task.task_id}</div>
                        </div>
                      </div>
                    </td>
                    <td className="px-6 py-4 text-sm text-gray-900">{task.assigned_to}</td>
                    <td className="px-6 py-4">
                      <span
                        className={`px-2 py-1 rounded text-xs font-medium ${
                          task.status === 'DONE'
                            ? 'bg-green-100 text-green-700'
                            : task.status === 'IN_PROGRESS'
                            ? 'bg-blue-100 text-blue-700'
                            : task.status === 'REVIEW'
                            ? 'bg-yellow-100 text-yellow-700'
                            : 'bg-gray-100 text-gray-700'
                        }`}
                      >
                        {task.status.replace('_', ' ')}
                      </span>
                    </td>
                    <td className="px-6 py-4">
                      <span
                        className={`px-2 py-1 rounded text-xs font-medium ${
                          task.priority === 'HIGH'
                            ? 'bg-red-100 text-red-700'
                            : task.priority === 'MEDIUM'
                            ? 'bg-yellow-100 text-yellow-700'
                            : 'bg-green-100 text-green-700'
                        }`}
                      >
                        {task.priority}
                      </span>
                    </td>
                    <td className="px-6 py-4 text-sm text-gray-900">
                      {new Date(task.expected_closure).toLocaleDateString()}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </div>
  );
};

export default ManagerDashboard;