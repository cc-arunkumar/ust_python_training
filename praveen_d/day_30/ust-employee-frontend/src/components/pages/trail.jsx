// import React, { useState, useEffect } from 'react';
// import { CheckCircle2, Circle, Clock, AlertCircle, Plus, Edit2, Trash2, User, Users, Settings, LogOut, ListTodo, FolderKanban, RefreshCw, ArrowLeft, Calendar, Tag } from 'lucide-react';

// // ============================================
// // CONFIGURATION
// // ============================================
// const API_BASE_URL = 'http://localhost:8000';

// // ============================================
// // API SERVICE
// // ============================================
// const api = {
//   login: async (emp_id, password) => {
//     const response = await fetch(`${API_BASE_URL}/auth/login`, {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify({ emp_id, password }),
//     });
//     if (!response.ok) {
//       const error = await response.json().catch(() => ({}));
//       throw new Error(error.detail || 'Login failed');
//     }
//     return response.json();
//   },

//   getTasks: async () => {
//     const response = await fetch(`${API_BASE_URL}/tasks/`);
//     if (!response.ok) throw new Error('Failed to fetch tasks');
//     return response.json();
//   },

//   updateTaskStatus: async (taskId, status, remarks = '') => {
//     const response = await fetch(`${API_BASE_URL}/tasks/${taskId}`, {
//       method: 'PATCH',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify({ status_: status, remarks }),
//     });
//     if (!response.ok) throw new Error('Failed to update task');
//     return response.json();
//   },

//   getEmployees: async () => {
//     const response = await fetch(`${API_BASE_URL}/employees/`);
//     if (!response.ok) throw new Error('Failed to fetch employees');
//     return response.json();
//   },

//   createEmployee: async (employeeData) => {
//     const response = await fetch(`${API_BASE_URL}/employees/`, {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify(employeeData),
//     });
//     if (!response.ok) {
//       const error = await response.json().catch(() => ({}));
//       throw new Error(error.detail || 'Failed to create employee');
//     }
//     return response.json();
//   },

//   updateEmployee: async (empId, employeeData) => {
//     const response = await fetch(`${API_BASE_URL}/employees/${empId}`, {
//       method: 'PUT',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify(employeeData),
//     });
//     if (!response.ok) throw new Error('Failed to update employee');
//     return response.json();
//   },

//   deleteEmployee: async (empId) => {
//     const response = await fetch(`${API_BASE_URL}/employees/${empId}`, {
//       method: 'DELETE',
//     });
//     if (!response.ok) throw new Error('Failed to delete employee');
//     return response.json();
//   },

//   createTask: async (taskData) => {
//     const response = await fetch(`${API_BASE_URL}/tasks/`, {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify(taskData),
//     });
//     if (!response.ok) {
//       const error = await response.json().catch(() => ({}));
//       throw new Error(error.detail || 'Failed to create task');
//     }
//     return response.json();
//   },

//   reviewTask: async (taskId, remarks) => {
//     const response = await fetch(`${API_BASE_URL}/tasks/${taskId}/review?remarks=${encodeURIComponent(remarks)}`, {
//       method: 'PATCH',
//       headers: { 'Content-Type': 'application/json' },
//     });
//     if (!response.ok) throw new Error('Failed to review task');
//     return response.json();
//   },
// };

// // ============================================
// // TASK STATUS ICON COMPONENT
// // ============================================
// const TaskStatusIcon = ({ status }) => {
//   const icons = {
//     TO_DO: <Circle className="w-5 h-5 text-gray-500" />,
//     IN_PROGRESS: <Clock className="w-5 h-5 text-blue-500" />,
//     REVIEW: <AlertCircle className="w-5 h-5 text-amber-500" />,
//     DONE: <CheckCircle2 className="w-5 h-5 text-emerald-500" />,
//   };
//   return icons[status] || <Circle className="w-5 h-5 text-gray-400" />;
// };

// // ============================================
// // TASK CARD COMPONENT
// // ============================================
// const TaskCard = ({ task, onRefresh, canEdit = true }) => {
//   const [isExpanded, setIsExpanded] = useState(false);
//   const [newStatus, setNewStatus] = useState(task.status);
//   const [isUpdating, setIsUpdating] = useState(false);

//   const handleStatusChange = async (e) => {
//     const selectedStatus = e.target.value;
//     setNewStatus(selectedStatus);
    
//     if (selectedStatus !== task.status && canEdit) {
//       setIsUpdating(true);
//       try {
//         await api.updateTaskStatus(task.task_id, selectedStatus, '');
//         if (onRefresh) await onRefresh();
//       } catch (err) {
//         console.error('Failed to update:', err);
//         setNewStatus(task.status);
//       } finally {
//         setIsUpdating(false);
//       }
//     }
//   };

//   const priorityConfig = {
//     HIGH: { bg: 'bg-gradient-to-r from-red-500 to-pink-500', text: 'text-white', border: 'border-red-300' },
//     MEDIUM: { bg: 'bg-gradient-to-r from-amber-400 to-orange-400', text: 'text-white', border: 'border-amber-300' },
//     LOW: { bg: 'bg-gradient-to-r from-emerald-400 to-teal-400', text: 'text-white', border: 'border-emerald-300' },
//   };

//   const statusConfig = {
//     TO_DO: { bg: 'bg-gradient-to-br from-gray-50 to-gray-100', border: 'border-gray-300' },
//     IN_PROGRESS: { bg: 'bg-gradient-to-br from-blue-50 to-indigo-50', border: 'border-blue-300' },
//     REVIEW: { bg: 'bg-gradient-to-br from-amber-50 to-yellow-50', border: 'border-amber-300' },
//     DONE: { bg: 'bg-gradient-to-br from-emerald-50 to-teal-50', border: 'border-emerald-300' },
//   };

//   const config = statusConfig[task.status] || statusConfig.TO_DO;
//   const priorityStyle = priorityConfig[task.priority] || priorityConfig.MEDIUM;

//   return (
//     <div className={`${config.bg} rounded-xl border-2 ${config.border} p-4 hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1`}>
//       <div className="flex items-start justify-between mb-3">
//         <div className="flex items-start space-x-3 flex-1 min-w-0">
//           <div className="mt-1">
//             <TaskStatusIcon status={task.status} />
//           </div>
//           <div className="flex-1 min-w-0">
//             <h3 className="font-bold text-gray-900 text-sm leading-tight mb-1">{task.name}</h3>
//             <p className="text-xs text-gray-600 font-mono">{task.task_id}</p>
//           </div>
//         </div>
//         <div className={`${priorityStyle.bg} px-3 py-1 rounded-full text-xs font-bold ${priorityStyle.text} shadow-md ml-2 shrink-0`}>
//           {task.priority}
//         </div>
//       </div>

//       {isExpanded && (
//         <div className="mb-3 space-y-3 pt-3 border-t-2 border-white">
//           <p className="text-sm text-gray-700 bg-white rounded-lg p-3 shadow-sm">{task.description}</p>
//           <div className="grid grid-cols-2 gap-2 text-xs">
//             <div className="bg-white rounded-lg p-2 shadow-sm">
//               <div className="flex items-center text-gray-500 font-semibold mb-1">
//                 <Calendar className="w-3 h-3 mr-1" />
//                 <span>Due Date</span>
//               </div>
//               <p className="text-gray-900 font-medium">{new Date(task.expected_closure).toLocaleDateString()}</p>
//             </div>
//             <div className="bg-white rounded-lg p-2 shadow-sm">
//               <div className="flex items-center text-gray-500 font-semibold mb-1">
//                 <User className="w-3 h-3 mr-1" />
//                 <span>Assigned By</span>
//               </div>
//               <p className="text-gray-900 font-medium">{task.assigned_by}</p>
//             </div>
//           </div>
//           {task.remarks && (
//             <div className="bg-gradient-to-r from-blue-50 to-indigo-50 border-2 border-blue-200 rounded-lg p-3 shadow-sm">
//               <p className="text-xs text-blue-700 font-semibold mb-1">💬 Remarks:</p>
//               <p className="text-xs text-blue-900">{task.remarks}</p>
//             </div>
//           )}
//         </div>
//       )}

//       <div className="flex items-center justify-between pt-3 border-t-2 border-white">
//         <select
//           value={newStatus}
//           onChange={handleStatusChange}
//           disabled={isUpdating || !canEdit}
//           className={`text-xs font-semibold border-2 rounded-lg px-3 py-2 focus:ring-2 focus:ring-indigo-500 transition-all ${
//             isUpdating ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer hover:bg-white'
//           } ${
//             newStatus === 'TO_DO' ? 'bg-gray-100 border-gray-300 text-gray-700' :
//             newStatus === 'IN_PROGRESS' ? 'bg-blue-100 border-blue-300 text-blue-700' :
//             newStatus === 'REVIEW' ? 'bg-amber-100 border-amber-300 text-amber-700' :
//             'bg-emerald-100 border-emerald-300 text-emerald-700'
//           }`}
//         >
//           <option value="TO_DO">📋 To Do</option>
//           <option value="IN_PROGRESS">⚡ In Progress</option>
//           <option value="REVIEW">👀 Review</option>
//           <option value="DONE">✅ Done</option>
//         </select>
//         <button
//           onClick={() => setIsExpanded(!isExpanded)}
//           className="text-xs font-bold text-indigo-600 hover:text-indigo-800 bg-white px-3 py-2 rounded-lg shadow-sm hover:shadow-md transition-all"
//         >
//           {isExpanded ? '▲ Less' : '▼ More'}
//         </button>
//       </div>
//     </div>
//   );
// };

// // ============================================
// // MAIN APP COMPONENT
// // ============================================
// const App = () => {
//   const [currentView, setCurrentView] = useState('login');
//   const [user, setUser] = useState(null);
//   const [selectedRole, setSelectedRole] = useState(null);
//   const [tasks, setTasks] = useState([]);
//   const [employees, setEmployees] = useState([]);
//   const [loading, setLoading] = useState(false);
//   const [error, setError] = useState('');

//   useEffect(() => {
//     if (currentView === 'dashboard') {
//       if (selectedRole === 'EMPLOYEE' || selectedRole === 'MANAGER') {
//         loadTasks();
//       }
//       if (selectedRole === 'ADMIN') {
//         loadEmployees();
//       }
//     }
//   }, [currentView, selectedRole]);

//   const loadTasks = async () => {
//     try {
//       const data = await api.getTasks();
//       setTasks(data);
//     } catch (err) {
//       console.error('Failed to load tasks:', err);
//     }
//   };

//   const loadEmployees = async () => {
//     try {
//       const data = await api.getEmployees();
//       setEmployees(data);
//     } catch (err) {
//       console.error('Failed to load employees:', err);
//     }
//   };

//   // ============================================
//   // LOGIN PAGE
//   // ============================================
//   const LoginPage = () => {
//     const [empId, setEmpId] = useState('');
//     const [password, setPassword] = useState('');
//     const [loginError, setLoginError] = useState('');
//     const [isLoading, setIsLoading] = useState(false);

//     const handleLogin = async (e) => {
//       e.preventDefault();
//       setLoginError('');
//       setIsLoading(true);

//       try {
//         const response = await api.login(empId, password);
        
//         setUser({
//           emp_id: response.emp_id || empId,
//           role: response.role,
//           name: empId,
//         });

//         if (response.role === 'ADMIN' || response.role === 'MANAGER') {
//           setCurrentView('roleSelector');
//         } else {
//           setSelectedRole('EMPLOYEE');
//           setCurrentView('dashboard');
//         }
//       } catch (err) {
//         setLoginError(err.message || 'Invalid credentials');
//       } finally {
//         setIsLoading(false);
//       }
//     };

//     return (
//       <div className="min-h-screen bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center p-4">
//         <div className="bg-white rounded-3xl shadow-2xl w-full max-w-md p-8 transform hover:scale-105 transition-transform">
//           <div className="text-center mb-8">
//             <div className="inline-flex items-center justify-center w-20 h-20 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-2xl mb-4 shadow-lg transform hover:rotate-6 transition-transform">
//               <FolderKanban className="w-10 h-10 text-white" />
//             </div>
//             <h1 className="text-3xl font-black text-gray-900 mb-2 bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
//               UST Task Manager
//             </h1>
//             <p className="text-gray-600 font-medium">Employee Management System</p>
//           </div>

//           <form onSubmit={handleLogin} className="space-y-5">
//             <div>
//               <label className="block text-sm font-bold text-gray-700 mb-2">Employee ID</label>
//               <input
//                 type="text"
//                 value={empId}
//                 onChange={(e) => setEmpId(e.target.value)}
//                 className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all"
//                 placeholder="Enter your employee ID"
//                 required
//               />
//             </div>

//             <div>
//               <label className="block text-sm font-bold text-gray-700 mb-2">Password</label>
//               <input
//                 type="password"
//                 value={password}
//                 onChange={(e) => setPassword(e.target.value)}
//                 className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-all"
//                 placeholder="Enter your password"
//                 required
//               />
//             </div>

//             {loginError && (
//               <div className="bg-red-50 border-2 border-red-300 text-red-700 px-4 py-3 rounded-xl text-sm flex items-start shadow-md">
//                 <AlertCircle className="w-5 h-5 mr-2 shrink-0 mt-0.5" />
//                 <span>{loginError}</span>
//               </div>
//             )}

//             <button
//               type="submit"
//               disabled={isLoading}
//               className="w-full bg-gradient-to-r from-indigo-600 to-purple-600 text-white py-3 rounded-xl font-bold hover:from-indigo-700 hover:to-purple-700 transition-all shadow-lg hover:shadow-xl disabled:opacity-50 transform hover:scale-105"
//             >
//               {isLoading ? (
//                 <span className="flex items-center justify-center">
//                   <RefreshCw className="w-5 h-5 mr-2 animate-spin" />
//                   Signing in...
//                 </span>
//               ) : (
//                 '🚀 Sign In'
//               )}
//             </button>
//           </form>

//           <div className="mt-6 p-4 bg-gradient-to-r from-indigo-50 to-purple-50 rounded-xl border-2 border-indigo-200">
//             <p className="text-xs text-gray-700 text-center font-bold mb-2">🔑 Test Credentials:</p>
//             <div className="text-xs text-gray-600 space-y-1">
//               <p>👤 Employee: <code className="bg-white px-2 py-1 rounded font-mono font-bold">EMP001</code></p>
//               <p>👥 Manager: <code className="bg-white px-2 py-1 rounded font-mono font-bold">MGR001</code></p>
//               <p>⚙️ Admin: <code className="bg-white px-2 py-1 rounded font-mono font-bold">ADM001</code></p>
//               <p className="text-center mt-2">Password: <code className="bg-white px-2 py-1 rounded font-mono font-bold">password</code></p>
//             </div>
//           </div>
//         </div>
//       </div>
//     );
//   };

//   // ============================================
//   // ROLE SELECTOR
//   // ============================================
//   const RoleSelector = () => {
//     const handleRoleSelect = (role) => {
//       setSelectedRole(role);
//       setCurrentView('dashboard');
//     };

//     return (
//       <div className="min-h-screen bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 flex items-center justify-center p-4">
//         <div className="bg-white rounded-3xl shadow-2xl w-full max-w-3xl p-8">
//           <div className="text-center mb-8">
//             <h2 className="text-3xl font-black text-gray-900 mb-2">Welcome Back! 👋</h2>
//             <p className="text-gray-600 font-medium">Select your role to continue</p>
//           </div>

//           <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
//             {user?.role === 'ADMIN' && (
//               <button
//                 onClick={() => handleRoleSelect('ADMIN')}
//                 className="p-8 border-2 border-gray-200 rounded-2xl hover:border-indigo-500 hover:bg-gradient-to-br hover:from-indigo-50 hover:to-purple-50 transition-all group transform hover:scale-105 hover:shadow-xl"
//               >
//                 <div className="flex flex-col items-center">
//                   <div className="w-20 h-20 bg-gradient-to-br from-indigo-400 to-purple-500 rounded-2xl flex items-center justify-center mb-4 shadow-lg group-hover:scale-110 transition-transform">
//                     <Settings className="w-10 h-10 text-white" />
//                   </div>
//                   <h3 className="text-xl font-black text-gray-900 mb-2">⚙️ Admin Panel</h3>
//                   <p className="text-gray-600 text-center text-sm font-medium">
//                     Manage employees and system configuration
//                   </p>
//                 </div>
//               </button>
//             )}

//             {(user?.role === 'MANAGER' || user?.role === 'ADMIN') && (
//               <button
//                 onClick={() => handleRoleSelect('MANAGER')}
//                 className="p-8 border-2 border-gray-200 rounded-2xl hover:border-emerald-500 hover:bg-gradient-to-br hover:from-emerald-50 hover:to-teal-50 transition-all group transform hover:scale-105 hover:shadow-xl"
//               >
//                 <div className="flex flex-col items-center">
//                   <div className="w-20 h-20 bg-gradient-to-br from-emerald-400 to-teal-500 rounded-2xl flex items-center justify-center mb-4 shadow-lg group-hover:scale-110 transition-transform">
//                     <Users className="w-10 h-10 text-white" />
//                   </div>
//                   <h3 className="text-xl font-black text-gray-900 mb-2">👥 Manager Dashboard</h3>
//                   <p className="text-gray-600 text-center text-sm font-medium">
//                     Create tasks and manage team progress
//                   </p>
//                 </div>
//               </button>
//             )}
//           </div>

//           <div className="mt-8 text-center">
//             <button
//               onClick={() => {
//                 setUser(null);
//                 setCurrentView('login');
//               }}
//               className="text-gray-600 hover:text-gray-900 text-sm flex items-center justify-center mx-auto font-semibold hover:underline"
//             >
//               <ArrowLeft className="w-4 h-4 mr-1" />
//               Back to Login
//             </button>
//           </div>
//         </div>
//       </div>
//     );
//   };

//   // ============================================
//   // EMPLOYEE DASHBOARD
//   // ============================================
//   const EmployeeDashboard = () => {
//     const myTasks = tasks.filter(t => t.assigned_to === user?.emp_id);
//     const tasksByStatus = {
//       TO_DO: myTasks.filter(t => t.status === 'TO_DO'),
//       IN_PROGRESS: myTasks.filter(t => t.status === 'IN_PROGRESS'),
//       REVIEW: myTasks.filter(t => t.status === 'REVIEW'),
//       DONE: myTasks.filter(t => t.status === 'DONE'),
//     };

//     const statusConfig = {
//       TO_DO: { label: '📋 To Do', bg: 'bg-gradient-to-br from-gray-100 to-gray-200', border: 'border-gray-400', count: 'bg-gray-600' },
//       IN_PROGRESS: { label: '⚡ In Progress', bg: 'bg-gradient-to-br from-blue-100 to-indigo-200', border: 'border-blue-400', count: 'bg-blue-600' },
//       REVIEW: { label: '👀 Review', bg: 'bg-gradient-to-br from-amber-100 to-yellow-200', border: 'border-amber-400', count: 'bg-amber-600' },
//       DONE: { label: '✅ Done', bg: 'bg-gradient-to-br from-emerald-100 to-teal-200', border: 'border-emerald-400', count: 'bg-emerald-600' },
//     };

//     const handleCreateTask = async (e) => {
//       e.preventDefault();
//       setLoading(true);
//       try {
//         const newTask = {
//           ...taskForm,
//           status: 'TO_DO',
//           assigned_by: user?.emp_id,
//           created_by: user?.emp_id,
//           reviewer: user?.emp_id,
//         };
//         await api.createTask(newTask);
//         await loadTasks();
//         setShowCreateTask(false);
//         setTaskForm({
//           task_id: '',
//           name: '',
//           description: '',
//           assigned_to: '',
//           priority: 'MEDIUM',
//           expected_closure: '',
//         });
//         setError('');
//       } catch (err) {
//         setError(err.message);
//       } finally {
//         setLoading(false);
//       }
//     };

//     const handleReviewTask = async () => {
//       setLoading(true);
//       try {
//         await api.reviewTask(selectedTask.task_id, reviewRemarks);
//         await loadTasks();
//         setShowReviewModal(false);
//         setSelectedTask(null);
//         setReviewRemarks('');
//       } catch (err) {
//         setError(err.message);
//       } finally {
//         setLoading(false);
//       }
//     };

//     return (
//       <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
//         <header className="bg-white border-b-4 border-emerald-500 sticky top-0 z-10 shadow-lg">
//           <div className="max-w-7xl mx-auto px-4 py-4">
//             <div className="flex items-center justify-between">
//               <div className="flex items-center space-x-3">
//                 <div className="w-14 h-14 bg-gradient-to-br from-emerald-500 to-teal-600 rounded-xl flex items-center justify-center shadow-lg">
//                   <Users className="w-8 h-8 text-white" />
//                 </div>
//                 <div>
//                   <h1 className="text-2xl font-black text-gray-900">Manager Dashboard</h1>
//                   <p className="text-sm text-gray-600 font-semibold">{user?.emp_id}</p>
//                 </div>
//               </div>
//               <div className="flex items-center space-x-3">
//                 {user?.role === 'ADMIN' && (
//                   <button
//                     onClick={() => setCurrentView('roleSelector')}
//                     className="text-sm font-bold text-gray-700 bg-white hover:bg-gray-100 px-4 py-2 rounded-xl border-2 border-gray-300 transition-all"
//                   >
//                     🔄 Switch Role
//                   </button>
//                 )}
//                 <button
//                   onClick={loadTasks}
//                   className="p-3 text-white bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 rounded-xl shadow-md"
//                 >
//                   <RefreshCw className="w-5 h-5" />
//                 </button>
//                 <button
//                   onClick={() => {
//                     setUser(null);
//                     setSelectedRole(null);
//                     setCurrentView('login');
//                     setTasks([]);
//                   }}
//                   className="flex items-center space-x-2 text-white bg-gradient-to-r from-red-500 to-pink-500 px-4 py-3 rounded-xl font-bold shadow-md"
//                 >
//                   <LogOut className="w-5 h-5" />
//                   <span>Logout</span>
//                 </button>
//               </div>
//             </div>
//           </div>
//         </header>

//         <main className="max-w-7xl mx-auto px-4 py-8">
//           {error && (
//             <div className="mb-6 bg-red-50 border-2 border-red-300 text-red-700 px-4 py-3 rounded-xl flex items-start shadow-lg">
//               <AlertCircle className="w-5 h-5 mr-2 shrink-0 mt-0.5" />
//               <span className="font-semibold">{error}</span>
//             </div>
//           )}

//           <div className="mb-6">
//             <button
//               onClick={() => setShowCreateTask(true)}
//               className="bg-gradient-to-r from-emerald-500 to-teal-500 text-white px-6 py-4 rounded-xl hover:from-emerald-600 hover:to-teal-600 flex items-center space-x-2 font-black shadow-lg hover:shadow-xl transition-all transform hover:scale-105 text-lg"
//             >
//               <Plus className="w-6 h-6" />
//               <span>➕ Create New Task</span>
//             </button>
//           </div>

//           {showCreateTask && (
//             <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
//               <div className="bg-white rounded-2xl max-w-2xl w-full p-8 shadow-2xl max-h-[90vh] overflow-y-auto">
//                 <h3 className="text-3xl font-black mb-6 text-gray-900 bg-gradient-to-r from-emerald-600 to-teal-600 bg-clip-text text-transparent">
//                   ➕ Create New Task
//                 </h3>
//                 <form onSubmit={handleCreateTask} className="space-y-5">
//                   <div className="grid grid-cols-2 gap-4">
//                     <div>
//                       <label className="block text-sm font-bold text-gray-700 mb-2">Task ID *</label>
//                       <input
//                         type="text"
//                         value={taskForm.task_id}
//                         onChange={(e) => setTaskForm({ ...taskForm, task_id: e.target.value })}
//                         className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500"
//                         placeholder="TSK-001"
//                         required
//                       />
//                     </div>
//                     <div>
//                       <label className="block text-sm font-bold text-gray-700 mb-2">Priority *</label>
//                       <select
//                         value={taskForm.priority}
//                         onChange={(e) => setTaskForm({ ...taskForm, priority: e.target.value })}
//                         className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:ring-2 focus:ring-emerald-500"
//                       >
//                         <option value="HIGH">🔴 High</option>
//                         <option value="MEDIUM">🟡 Medium</option>
//                         <option value="LOW">🟢 Low</option>
//                       </select>
//                     </div>
//                   </div>
//                   <div>
//                     <label className="block text-sm font-bold text-gray-700 mb-2">Task Name *</label>
//                     <input
//                       type="text"
//                       value={taskForm.name}
//                       onChange={(e) => setTaskForm({ ...taskForm, name: e.target.value })}
//                       className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:ring-2 focus:ring-emerald-500"
//                       placeholder="Enter task name"
//                       required
//                     />
//                   </div>
//                   <div>
//                     <label className="block text-sm font-bold text-gray-700 mb-2">Description *</label>
//                     <textarea
//                       value={taskForm.description}
//                       onChange={(e) => setTaskForm({ ...taskForm, description: e.target.value })}
//                       className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:ring-2 focus:ring-emerald-500"
//                       rows="4"
//                       placeholder="Describe the task"
//                       required
//                     />
//                   </div>
//                   <div className="grid grid-cols-2 gap-4">
//                     <div>
//                       <label className="block text-sm font-bold text-gray-700 mb-2">Assign To (Employee ID) *</label>
//                       <input
//                         type="text"
//                         value={taskForm.assigned_to}
//                         onChange={(e) => setTaskForm({ ...taskForm, assigned_to: e.target.value })}
//                         className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:ring-2 focus:ring-emerald-500"
//                         placeholder="EMP001"
//                         required
//                       />
//                     </div>
//                     <div>
//                       <label className="block text-sm font-bold text-gray-700 mb-2">Due Date *</label>
//                       <input
//                         type="date"
//                         value={taskForm.expected_closure}
//                         onChange={(e) => setTaskForm({ ...taskForm, expected_closure: e.target.value })}
//                         className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:ring-2 focus:ring-emerald-500"
//                         required
//                       />
//                     </div>
//                   </div>
//                   <div className="flex justify-end space-x-3 pt-4 border-t-2 border-gray-200">
//                     <button
//                       type="button"
//                       onClick={() => setShowCreateTask(false)}
//                       className="px-6 py-3 border-2 border-gray-300 rounded-xl hover:bg-gray-50 font-bold transition-all"
//                     >
//                       Cancel
//                     </button>
//                     <button
//                       type="submit"
//                       disabled={loading}
//                       className="px-6 py-3 bg-gradient-to-r from-emerald-500 to-teal-500 text-white rounded-xl hover:from-emerald-600 hover:to-teal-600 font-bold shadow-md disabled:opacity-50"
//                     >
//                       {loading ? 'Creating...' : '✅ Create Task'}
//                     </button>
//                   </div>
//                 </form>
//               </div>
//             </div>
//           )}

//           {showReviewModal && selectedTask && (
//             <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
//               <div className="bg-white rounded-2xl max-w-2xl w-full p-8 shadow-2xl">
//                 <h3 className="text-3xl font-black mb-6 text-gray-900">👀 Review Task</h3>
//                 <div className="mb-6 p-4 bg-gradient-to-r from-amber-50 to-yellow-50 rounded-xl border-2 border-amber-200">
//                   <h4 className="font-bold text-gray-900 mb-2">{selectedTask.name}</h4>
//                   <p className="text-sm text-gray-700">{selectedTask.description}</p>
//                   <p className="text-xs text-gray-500 mt-2 font-mono">{selectedTask.task_id}</p>
//                 </div>
//                 <div>
//                   <label className="block text-sm font-bold text-gray-700 mb-2">Review Remarks *</label>
//                   <textarea
//                     value={reviewRemarks}
//                     onChange={(e) => setReviewRemarks(e.target.value)}
//                     className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:ring-2 focus:ring-amber-500"
//                     rows="5"
//                     placeholder="Add your review comments"
//                     required
//                   />
//                 </div>
//                 <div className="flex justify-end space-x-3 pt-6 border-t-2 border-gray-200 mt-6">
//                   <button
//                     onClick={() => {
//                       setShowReviewModal(false);
//                       setSelectedTask(null);
//                       setReviewRemarks('');
//                     }}
//                     className="px-6 py-3 border-2 border-gray-300 rounded-xl hover:bg-gray-50 font-bold"
//                   >
//                     Cancel
//                   </button>
//                   <button
//                     onClick={handleReviewTask}
//                     disabled={loading || !reviewRemarks}
//                     className="px-6 py-3 bg-gradient-to-r from-amber-500 to-yellow-500 text-white rounded-xl hover:from-amber-600 hover:to-yellow-600 font-bold shadow-md disabled:opacity-50"
//                   >
//                     {loading ? 'Submitting...' : '✅ Submit Review'}
//                   </button>
//                 </div>
//               </div>
//             </div>
//           )}

//           <div className="mb-6 bg-white rounded-xl shadow-lg p-4 border-2 border-gray-200">
//             <h2 className="text-xl font-black text-gray-900">📊 Team Tasks Overview</h2>
//             <p className="text-sm text-gray-600 mt-1">
//               Total: <span className="font-bold text-emerald-600">{relevantTasks.length}</span> tasks under your management
//             </p>
//           </div>

//           <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
//             {Object.entries(tasksByStatus).map(([status, statusTasks]) => {
//               const config = statusConfig[status];
//               return (
//                 <div key={status} className={`${config.bg} rounded-2xl border-2 ${config.border} p-5 shadow-lg`}>
//                   <div className="flex items-center justify-between mb-4">
//                     <h2 className="font-black text-gray-900 flex items-center space-x-2 text-lg">
//                       <TaskStatusIcon status={status} />
//                       <span>{config.label}</span>
//                     </h2>
//                     <span className={`${config.count} text-white px-4 py-2 rounded-full text-sm font-black shadow-md`}>
//                       {statusTasks.length}
//                     </span>
//                   </div>
//                   <div className="space-y-4 max-h-96 overflow-y-auto pr-2">
//                     {statusTasks.length > 0 ? (
//                       statusTasks.map(task => (
//                         <div key={task.task_id}>
//                           <TaskCard
//                             task={task}
//                             onRefresh={loadTasks}
//                             canEdit={true}
//                           />
//                           {task.status === 'REVIEW' && (
//                             <button
//                               onClick={() => {
//                                 setSelectedTask(task);
//                                 setReviewRemarks(task.remarks || '');
//                                 setShowReviewModal(true);
//                               }}
//                               className="w-full mt-2 bg-gradient-to-r from-amber-500 to-yellow-500 text-white px-3 py-2 rounded-lg font-bold text-sm hover:from-amber-600 hover:to-yellow-600 shadow-md"
//                             >
//                               👀 Review This Task
//                             </button>
//                           )}
//                         </div>
//                       ))
//                     ) : (
//                       <div className="text-center py-12 text-gray-400">
//                         <Circle className="w-12 h-12 mx-auto mb-3 opacity-30" />
//                         <p className="text-sm font-semibold">No tasks here</p>
//                       </div>
//                     )}
//                   </div>
//                 </div>
//               );
//             })}
//           </div>
//         </main>
//       </div>
//     );
//   };

//   // ============================================
//   // ADMIN DASHBOARD
//   // ============================================
//   const AdminDashboard = () => {
//     const [showCreateEmployee, setShowCreateEmployee] = useState(false);
//     const [showEditEmployee, setShowEditEmployee] = useState(false);
//     const [selectedEmployee, setSelectedEmployee] = useState(null);
//     const [employeeForm, setEmployeeForm] = useState({
//       emp_id: '',
//       name: '',
//       email: '',
//       designation: '',
//       mgr_id: '',
//     });

//     const handleCreateEmployee = async (e) => {
//       e.preventDefault();
//       setLoading(true);
//       try {
//         await api.createEmployee(employeeForm);
//         await loadEmployees();
//         setShowCreateEmployee(false);
//         setEmployeeForm({ emp_id: '', name: '', email: '', designation: '', mgr_id: '' });
//       } catch (err) {
//         setError(err.message);
//       } finally {
//         setLoading(false);
//       }
//     };

//     const handleEditEmployee = async (e) => {
//       e.preventDefault();
//       setLoading(true);
//       try {
//         await api.updateEmployee(employeeForm.emp_id, employeeForm);
//         await loadEmployees();
//         setShowEditEmployee(false);
//         setSelectedEmployee(null);
//       } catch (err) {
//         setError(err.message);
//       } finally {
//         setLoading(false);
//       }
//     };

//     const handleDeleteEmployee = async (empId) => {
//       if (window.confirm('Are you sure you want to delete this employee?')) {
//         setLoading(true);
//         try {
//           await api.deleteEmployee(empId);
//           await loadEmployees();
//         } catch (err) {
//           setError(err.message);
//         } finally {
//           setLoading(false);
//         }
//       }
//     };

//     return (
//       <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
//         <header className="bg-white border-b-4 border-indigo-500 sticky top-0 z-10 shadow-lg">
//           <div className="max-w-7xl mx-auto px-4 py-4">
//             <div className="flex items-center justify-between">
//               <div className="flex items-center space-x-3">
//                 <div className="w-14 h-14 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center shadow-lg">
//                   <Settings className="w-8 h-8 text-white" />
//                 </div>
//                 <div>
//                   <h1 className="text-2xl font-black text-gray-900">Admin Dashboard</h1>
//                   <p className="text-sm text-gray-600 font-semibold">{user?.emp_id}</p>
//                 </div>
//               </div>
//               <div className="flex items-center space-x-3">
//                 <button
//                   onClick={() => setCurrentView('roleSelector')}
//                   className="text-sm font-bold text-gray-700 bg-white hover:bg-gray-100 px-4 py-2 rounded-xl border-2 border-gray-300"
//                 >
//                   🔄 Switch Role
//                 </button>
//                 <button
//                   onClick={loadEmployees}
//                   className="p-3 text-white bg-gradient-to-r from-indigo-500 to-purple-500 rounded-xl shadow-md"
//                 >
//                   <RefreshCw className="w-5 h-5" />
//                 </button>
//                 <button
//                   onClick={() => {
//                     setUser(null);
//                     setSelectedRole(null);
//                     setCurrentView('login');
//                   }}
//                   className="flex items-center space-x-2 text-white bg-gradient-to-r from-red-500 to-pink-500 px-4 py-3 rounded-xl font-bold shadow-md"
//                 >
//                   <LogOut className="w-5 h-5" />
//                   <span>Logout</span>
//                 </button>
//               </div>
//             </div>
//           </div>
//         </header>

//         <main className="max-w-7xl mx-auto px-4 py-8">
//           {error && (
//             <div className="mb-6 bg-red-50 border-2 border-red-300 text-red-700 px-4 py-3 rounded-xl flex items-start shadow-lg">
//               <AlertCircle className="w-5 h-5 mr-2 shrink-0" />
//               <span className="font-semibold">{error}</span>
//             </div>
//           )}

//           <div className="mb-6">
//             <button
//               onClick={() => setShowCreateEmployee(true)}
//               className="bg-gradient-to-r from-indigo-500 to-purple-500 text-white px-6 py-4 rounded-xl flex items-center space-x-2 font-black shadow-lg hover:shadow-xl text-lg"
//             >
//               <Plus className="w-6 h-6" />
//               <span>➕ Create Employee</span>
//             </button>
//           </div>

//           <div className="bg-white rounded-2xl shadow-xl border-2 border-gray-200 overflow-hidden">
//             <div className="overflow-x-auto">
//               <table className="w-full">
//                 <thead className="bg-gradient-to-r from-indigo-500 to-purple-500 text-white">
//                   <tr>
//                     <th className="px-6 py-4 text-left text-sm font-black uppercase">Employee ID</th>
//                     <th className="px-6 py-4 text-left text-sm font-black uppercase">Name</th>
//                     <th className="px-6 py-4 text-left text-sm font-black uppercase">Email</th>
//                     <th className="px-6 py-4 text-left text-sm font-black uppercase">Designation</th>
//                     <th className="px-6 py-4 text-left text-sm font-black uppercase">Manager</th>
//                     <th className="px-6 py-4 text-left text-sm font-black uppercase">Actions</th>
//                   </tr>
//                 </thead>
//                 <tbody className="divide-y-2 divide-gray-200">
//                   {employees.length === 0 ? (
//                     <tr>
//                       <td colSpan="6" className="px-6 py-12 text-center text-gray-500">
//                         <User className="w-16 h-16 mx-auto mb-3 text-gray-300" />
//                         <p className="font-bold">No employees found</p>
//                       </td>
//                     </tr>
//                   ) : (
//                     employees.map((emp) => (
//                       <tr key={emp.emp_id} className="hover:bg-indigo-50 transition-colors">
//                         <td className="px-6 py-4 text-sm font-bold text-gray-900">{emp.emp_id}</td>
//                         <td className="px-6 py-4 text-sm font-semibold text-gray-900">{emp.name}</td>
//                         <td className="px-6 py-4 text-sm text-gray-700">{emp.email}</td>
//                         <td className="px-6 py-4 text-sm text-gray-700">{emp.designation}</td>
//                         <td className="px-6 py-4 text-sm text-gray-700">{emp.mgr_id || '-'}</td>
//                         <td className="px-6 py-4">
//                           <div className="flex items-center space-x-2">
//                             <button
//                               onClick={() => {
//                                 setSelectedEmployee(emp);
//                                 setEmployeeForm(emp);
//                                 setShowEditEmployee(true);
//                               }}
//                               className="text-indigo-600 hover:text-indigo-900 p-2 rounded-lg hover:bg-indigo-100"
//                             >
//                               <Edit2 className="w-5 h-5" />
//                             </button>
//                             <button
//                               onClick={() => handleDeleteEmployee(emp.emp_id)}
//                               className="text-red-600 hover:text-red-900 p-2 rounded-lg hover:bg-red-100"
//                             >
//                               <Trash2 className="w-5 h-5" />
//                             </button>
//                           </div>
//                         </td>
//                       </tr>
//                     ))
//                   )}
//                 </tbody>
//               </table>
//             </div>
//           </div>
//         </main>
//       </div>
//     );
//   };

//   // ============================================
//   // MAIN RENDER
//   // ============================================
//   return (
//     <div>
//       {currentView === 'login' && <LoginPage />}
//       {currentView === 'roleSelector' && <RoleSelector />}
//       {currentView === 'dashboard' && selectedRole === 'EMPLOYEE' && <EmployeeDashboard />}
//       {currentView === 'dashboard' && selectedRole === 'MANAGER' && <ManagerDashboard />}
//       {currentView === 'dashboard' && selectedRole === 'ADMIN' && <AdminDashboard />}
//     </div>
//   );
// };

// export default App;'bg-amber-600' },
//       DONE: { label: '✅ Done', bg: 'bg-gradient-to-br from-emerald-100 to-teal-200', border: 'border-emerald-400', count: 'bg-emerald-600' },
//     };

//     return (
//       <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
//         <header className="bg-white border-b-4 border-indigo-500 sticky top-0 z-10 shadow-lg">
//           <div className="max-w-7xl mx-auto px-4 py-4">
//             <div className="flex items-center justify-between">
//               <div className="flex items-center space-x-3">
//                 <div className="w-14 h-14 bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center shadow-lg">
//                   <FolderKanban className="w-8 h-8 text-white" />
//                 </div>
//                 <div>
//                   <h1 className="text-2xl font-black text-gray-900">My Tasks</h1>
//                   <p className="text-sm text-gray-600 font-semibold">Welcome back, {user?.emp_id}</p>
//                 </div>
//               </div>
//               <div className="flex items-center space-x-3">
//                 <button
//                   onClick={loadTasks}
//                   className="p-3 text-white bg-gradient-to-r from-indigo-500 to-purple-500 hover:from-indigo-600 hover:to-purple-600 rounded-xl shadow-md hover:shadow-lg transition-all"
//                   title="Refresh"
//                 >
//                   <RefreshCw className="w-5 h-5" />
//                 </button>
//                 <button
//                   onClick={() => {
//                     setUser(null);
//                     setSelectedRole(null);
//                     setCurrentView('login');
//                     setTasks([]);
//                   }}
//                   className="flex items-center space-x-2 text-white bg-gradient-to-r from-red-500 to-pink-500 hover:from-red-600 hover:to-pink-600 px-4 py-3 rounded-xl font-bold shadow-md hover:shadow-lg transition-all"
//                 >
//                   <LogOut className="w-5 h-5" />
//                   <span>Logout</span>
//                 </button>
//               </div>
//             </div>
//           </div>
//         </header>

//         <main className="max-w-7xl mx-auto px-4 py-8">
//           {error && (
//             <div className="mb-6 bg-red-50 border-2 border-red-300 text-red-700 px-4 py-3 rounded-xl flex items-start shadow-lg">
//               <AlertCircle className="w-5 h-5 mr-2 shrink-0 mt-0.5" />
//               <span className="font-semibold">{error}</span>
//             </div>
//           )}

//           <div className="mb-6 bg-white rounded-xl shadow-lg p-4 border-2 border-gray-200">
//             <h2 className="text-xl font-black text-gray-900">📊 Task Board</h2>
//             <p className="text-sm text-gray-600 mt-1">
//               Total: <span className="font-bold text-indigo-600">{myTasks.length}</span> tasks assigned to you
//             </p>
//           </div>

//           <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
//             {Object.entries(tasksByStatus).map(([status, statusTasks]) => {
//               const config = statusConfig[status];
//               return (
//                 <div key={status} className={`${config.bg} rounded-2xl border-2 ${config.border} p-5 shadow-lg`}>
//                   <div className="flex items-center justify-between mb-4">
//                     <h2 className="font-black text-gray-900 flex items-center space-x-2 text-lg">
//                       <TaskStatusIcon status={status} />
//                       <span>{config.label}</span>
//                     </h2>
//                     <span className={`${config.count} text-white px-4 py-2 rounded-full text-sm font-black shadow-md`}>
//                       {statusTasks.length}
//                     </span>
//                   </div>
//                   <div className="space-y-4 max-h-96 overflow-y-auto pr-2">
//                     {statusTasks.length > 0 ? (
//                       statusTasks.map(task => (
//                         <TaskCard
//                           key={task.task_id}
//                           task={task}
//                           onRefresh={loadTasks}
//                           canEdit={true}
//                         />
//                       ))
//                     ) : (
//                       <div className="text-center py-12 text-gray-400">
//                         <Circle className="w-12 h-12 mx-auto mb-3 opacity-30" />
//                         <p className="text-sm font-semibold">No tasks here</p>
//                       </div>
//                     )}
//                   </div>
//                 </div>
//               );
//             })}
//           </div>
//         </main>
//       </div>
//     );
//   };

//   // ============================================
//   // MANAGER DASHBOARD
//   // ============================================
//   const ManagerDashboard = () => {
//     const [showCreateTask, setShowCreateTask] = useState(false);
//     const [showReviewModal, setShowReviewModal] = useState(false);
//     const [selectedTask, setSelectedTask] = useState(null);
//     const [reviewRemarks, setReviewRemarks] = useState('');
//     const [taskForm, setTaskForm] = useState({
//       task_id: '',
//       name: '',
//       description: '',
//       assigned_to: '',
//       priority: 'MEDIUM',
//       expected_closure: '',
//     });

//     // Filter tasks - show all tasks if manager, or tasks assigned to/by manager
//     const relevantTasks = tasks.filter(t => 
//       t.assigned_by === user?.emp_id || t.reviewer === user?.emp_id || user?.role === 'ADMIN'
//     );

//     const tasksByStatus = {
//       TO_DO: relevantTasks.filter(t => t.status === 'TO_DO'),
//       IN_PROGRESS: relevantTasks.filter(t => t.status === 'IN_PROGRESS'),
//       REVIEW: relevantTasks.filter(t => t.status === 'REVIEW'),
//       DONE: relevantTasks.filter(t => t.status === 'DONE'),
//     };

//     const statusConfig = {
//       TO_DO: { label: '📋 To Do', bg: 'bg-gradient-to-br from-gray-100 to-gray-200', border: 'border-gray-400', count: 'bg-gray-600' },
//       IN_PROGRESS: { label: '⚡ In Progress', bg: 'bg-gradient-to-br from-blue-100 to-indigo-200', border: 'border-blue-400', count: 'bg-blue-600' },
//       REVIEW: { label: '👀 Review', bg: 'bg-gradient-to-br from-amber-100 to-yellow-200', border: 