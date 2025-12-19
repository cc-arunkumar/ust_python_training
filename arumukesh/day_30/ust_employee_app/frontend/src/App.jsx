import React, { createContext, useContext, useState, useEffect } from 'react';
import { ChevronDown, LogOut, Menu, X, CheckSquare, Users, UserPlus, Briefcase, Edit, Trash2 } from 'lucide-react';

// API Configuration
const API_BASE_URL = 'http://localhost:8000';

// Auth Context
const AuthContext = createContext(null);

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('token'));
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (token) {
      try {
        const payload = JSON.parse(atob(token.split('.')[1]));
        setUser(payload);
      } catch (e) {
        localStorage.removeItem('token');
        setToken(null);
      }
    }
    setLoading(false);
  }, [token]);

  const login = async (emp_id, password) => {
    const response = await fetch(`${API_BASE_URL}/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ emp_id, password })
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Login failed');
    }

    const data = await response.json();
    localStorage.setItem('token', data.access_token);
    setToken(data.access_token);
    setUser(data.user);
    return data;
  };

  const logout = () => {
    localStorage.removeItem('token');
    setToken(null);
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, token, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within AuthProvider');
  return context;
};

// API Helper
const apiCall = async (endpoint, method = 'GET', body = null, token = null) => {
  const headers = { 'Content-Type': 'application/json' };
  if (token) headers['Authorization'] = `Bearer ${token}`;

  const config = { method, headers };
  if (body) config.body = JSON.stringify(body);

  const response = await fetch(`${API_BASE_URL}${endpoint}`, config);
  
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || 'Request failed');
  }

  if (method === 'DELETE') return null;
  return response.json();
};

// Login Page
const LoginPage = () => {
  const [empId, setEmpId] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      await login(parseInt(empId), password);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
      <div className="bg-white rounded-lg shadow-xl p-8 w-full max-w-md">
        <div className="text-center mb-8">
          <div className="bg-indigo-600 w-16 h-16 rounded-lg flex items-center justify-center mx-auto mb-4">
            <CheckSquare className="text-white" size={32} />
          </div>
          <h1 className="text-3xl font-bold text-gray-800">Task Manager</h1>
          <p className="text-gray-600 mt-2">Sign in to your account</p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Employee ID</label>
            <input
              type="number"
              value={empId}
              onChange={(e) => setEmpId(e.target.value)}
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
              placeholder="Enter your employee ID"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
              placeholder="Enter your password"
              required
            />
          </div>

          {error && (
            <div className="bg-red-50 text-red-600 px-4 py-3 rounded-lg text-sm">{error}</div>
          )}

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-indigo-600 text-white py-3 rounded-lg font-medium hover:bg-indigo-700 transition disabled:opacity-50"
          >
            {loading ? 'Signing in...' : 'Sign In'}
          </button>
        </form>
      </div>
    </div>
  );
};

// Sidebar Component
const Sidebar = ({ activeView, setActiveView, sidebarOpen, setSidebarOpen }) => {
  const { user } = useAuth();
  const [expandedMenus, setExpandedMenus] = useState({ tasks: true });

  const toggleMenu = (menu) => {
    setExpandedMenus(prev => ({ ...prev, [menu]: !prev[menu] }));
  };

  const isAdmin = user?.role?.toLowerCase().includes('admin');
  const isManager = user?.role?.toLowerCase().includes('manager');

  const menuItems = [
    {
      id: 'tasks',
      icon: CheckSquare,
      label: 'Tasks',
      show: true,
      submenu: [
        { id: 'myTasks', label: 'My Tasks', show: true },
        { id: 'reviewTasks', label: 'Review Tasks', show: isManager || isAdmin },
        { id: 'createTask', label: 'Create Task', show: isManager || isAdmin }
      ]
    },
    {
      id: 'users',
      icon: Users,
      label: 'User Actions',
      show: isAdmin,
      submenu: [
        { id: 'createUser', label: 'Create User', show: true },
        { id: 'listUsers', label: 'List / Update / Delete Users', show: true }
      ]
    },
    {
      id: 'employees',
      icon: Briefcase,
      label: 'Employees',
      show: isAdmin,
      submenu: [
        { id: 'createEmployee', label: 'Create Employee', show: true },
        { id: 'listEmployees', label: 'List / Update / Delete Employees', show: true }
      ]
    }
  ];

  return (
    <>
      {sidebarOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-50 z-20 lg:hidden" onClick={() => setSidebarOpen(false)} />
      )}

      <div className={`fixed lg:static inset-y-0 left-0 z-30 w-64 bg-gray-900 text-white transform transition-transform duration-300 ease-in-out ${
        sidebarOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'
      }`}>
        <div className="p-4 border-b border-gray-800 flex items-center justify-between">
          <h2 className="text-xl font-bold">Menu</h2>
          <button onClick={() => setSidebarOpen(false)} className="lg:hidden text-gray-400 hover:text-white">
            <X size={24} />
          </button>
        </div>

        <nav className="p-4 space-y-2">
          {menuItems.map(item => {
            if (!item.show) return null;
            const Icon = item.icon;

            return (
              <div key={item.id}>
                <button
                  onClick={() => toggleMenu(item.id)}
                  className="w-full flex items-center justify-between px-4 py-3 rounded-lg hover:bg-gray-800 transition"
                >
                  <div className="flex items-center gap-3">
                    <Icon size={20} />
                    <span>{item.label}</span>
                  </div>
                  <ChevronDown size={16} className={`transform transition-transform ${expandedMenus[item.id] ? 'rotate-180' : ''}`} />
                </button>

                {expandedMenus[item.id] && (
                  <div className="ml-8 mt-1 space-y-1">
                    {item.submenu.map(sub => {
                      if (!sub.show) return null;
                      return (
                        <button
                          key={sub.id}
                          onClick={() => {
                            setActiveView(sub.id);
                            setSidebarOpen(false);
                          }}
                          className={`w-full text-left px-4 py-2 rounded-lg text-sm transition ${
                            activeView === sub.id ? 'bg-indigo-600 text-white' : 'text-gray-300 hover:bg-gray-800'
                          }`}
                        >
                          {sub.label}
                        </button>
                      );
                    })}
                  </div>
                )}
              </div>
            );
          })}
        </nav>
      </div>
    </>
  );
};

// Header
const Header = ({ sidebarOpen, setSidebarOpen }) => {
  const { user, logout } = useAuth();

  return (
    <header className="bg-white shadow-sm border-b border-gray-200 px-4 py-3">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-4">
          <button onClick={() => setSidebarOpen(!sidebarOpen)} className="lg:hidden text-gray-600 hover:text-gray-900">
            <Menu size={24} />
          </button>
          <h1 className="text-xl font-bold text-gray-800">Task Manager Dashboard</h1>
        </div>

        <div className="flex items-center gap-4">
          <div className="text-right">
            <p className="text-sm font-medium text-gray-800">Emp ID: {user?.emp_id}</p>
            <p className="text-xs text-gray-600 capitalize">{user?.role}</p>
          </div>
          <button onClick={logout} className="flex items-center gap-2 px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition">
            <LogOut size={16} />
            <span className="hidden sm:inline">Logout</span>
          </button>
        </div>
      </div>
    </header>
  );
};

// Dashboard Layout
const Dashboard = () => {
  const [activeView, setActiveView] = useState('myTasks');
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const renderView = () => {
    switch (activeView) {
      case 'myTasks': return <MyTasks />;
      case 'reviewTasks': return <ReviewTasks />;
      case 'createTask': return <CreateTask />;
      case 'createUser': return <CreateUser />;
      case 'listUsers': return <ListUsers />;
      case 'createEmployee': return <CreateEmployee />;
      case 'listEmployees': return <ListEmployees />;
      default: return <MyTasks />;
    }
  };

  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar activeView={activeView} setActiveView={setActiveView} sidebarOpen={sidebarOpen} setSidebarOpen={setSidebarOpen} />
      <div className="flex-1 flex flex-col overflow-hidden">
        <Header sidebarOpen={sidebarOpen} setSidebarOpen={setSidebarOpen} />
        <main className="flex-1 overflow-y-auto">
          {renderView()}
        </main>
      </div>
    </div>
  );
};

// My Tasks
const MyTasks = () => {
  const { token, user } = useAuth();
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const data = await apiCall('/api/v1/tasks', 'GET', null, token);
      setTasks(data.filter(t => t.assigned_to === user.emp_id));
    } catch (err) {
      alert(err.message);
    } finally {
      setLoading(false);
    }
  };

  const updateStatus = async (id, status) => {
    try {
      await apiCall(`/api/v1/tasks/${id}/status`, 'PATCH', { status }, token);
      fetchTasks();
    } catch (err) {
      alert(err.message);
    }
  };

  if (loading) return <div className="p-8 text-center">Loading tasks...</div>;

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-6">My Tasks</h2>
      {tasks.length === 0 ? <p className="text-gray-600">No tasks assigned.</p> : (
        <div className="space-y-4">
          {tasks.map(task => (
            <div key={task.t_id} className="bg-white p-6 rounded-lg shadow border">
              <div className="flex justify-between">
                <div>
                  <h3 className="font-bold text-lg">{task.title}</h3>
                  <p className="text-gray-600">{task.description}</p>
                </div>
                <span className={`px-3 py-1 rounded-full text-xs font-medium ${
                  task.priority === 'high' ? 'bg-red-100 text-red-800' :
                  task.priority === 'medium' ? 'bg-yellow-100 text-yellow-800' :
                  'bg-green-100 text-green-800'
                }`}>{task.priority.toUpperCase()}</span>
              </div>
              <div className="mt-4 flex justify-between items-center">
                <span className="text-sm text-gray-600">Status: <strong>{task.status.replace('_', ' ')}</strong></span>
                <select value={task.status} onChange={(e) => updateStatus(task.t_id, e.target.value)} className="border rounded px-3 py-1">
                  <option value="pending">Pending</option>
                  <option value="in_progress">In Progress</option>
                  <option value="completed">Completed</option>
                  <option value="on_hold">On Hold</option>
                  <option value="cancelled">Cancelled</option>
                </select>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

// Review Tasks (similar to MyTasks but filtered by reviewer)
const ReviewTasks = () => {
  const { token, user } = useAuth();
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => { fetchTasks(); }, []);

  const fetchTasks = async () => {
    try {
      const data = await apiCall('/api/v1/tasks', 'GET', null, token);
      setTasks(data.filter(t => t.reviewer === user.emp_id));
    } catch (err) { alert(err.message); } finally { setLoading(false); }
  };

  const updateStatus = async (id, status) => {
    try {
      await apiCall(`/api/v1/tasks/${id}/status`, 'PATCH', { status }, token);
      fetchTasks();
    } catch (err) { alert(err.message); }
  };

  if (loading) return <div className="p-8">Loading...</div>;

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-6">Tasks to Review</h2>
      {tasks.length === 0 ? <p>No tasks to review.</p> : (
        <div className="space-y-4">
          {tasks.map(task => (
            <div key={task.t_id} className="bg-white p-6 rounded-lg shadow border">
              <h3 className="font-bold text-lg">{task.title}</h3>
              <p className="text-gray-600 mb-4">{task.description}</p>
              <p><strong>Assigned to:</strong> {task.assigned_to}</p>
              <div className="mt-4 flex justify-between items-center">
                <span className="text-sm"><strong>Status:</strong> {task.status.replace('_', ' ')}</span>
                <select value={task.status} onChange={(e) => updateStatus(task.t_id, e.target.value)} className="border rounded px-3 py-1">
                  <option value="pending">Pending</option>
                  <option value="in_progress">In Progress</option>
                  <option value="completed">Completed</option>
                  <option value="on_hold">On Hold</option>
                  <option value="cancelled">Cancelled</option>
                </select>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

// Create Task
const CreateTask = () => {
  const { token, user } = useAuth();
  const [employees, setEmployees] = useState([]);
  const [form, setForm] = useState({
    title: '', description: '', assigned_to: '', reviewer: '',
    priority: 'medium', expected_closure: '', remarks: ''
  });

  useEffect(() => {
    apiCall('/api/v1/employees', 'GET', null, token).then(setEmployees).catch(console.error);
  }, [token]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await apiCall('/api/v1/tasks', 'POST', {
        ...form,
        created_by: user.emp_id,
        assigned_by: user.emp_id,
        status: 'pending'
      }, token);
      alert('Task created!');
      setForm({ title: '', description: '', assigned_to: '', reviewer: '', priority: 'medium', expected_closure: '', remarks: '' });
    } catch (err) {
      alert(err.message);
    }
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h2 className="text-2xl font-bold mb-6">Create New Task</h2>
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow space-y-4">
        {/* Form fields similar to earlier, omitted for brevity but same as before */}
        {/* Include title, desc, assigned_to, reviewer (managers only), priority, expected_closure, remarks */}
        <button type="submit" className="w-full bg-indigo-600 text-white py-3 rounded-lg hover:bg-indigo-700">Create Task</button>
      </form>
    </div>
  );
};

// Create Employee + Auto User Creation
const CreateEmployee = () => {
  const { token } = useAuth();
  const [form, setForm] = useState({
    emp_id: '', name: '', email: '', designation: '', mgr_id: '', password: '', role: 'developer'
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const { password, role, ...empData } = form;
      if (mgr_id === '') delete empData.mgr_id;

      await apiCall('/api/v1/employees', 'POST', empData, token);
      await apiCall('/api/v1/users', 'POST', {
        emp_id: parseInt(form.emp_id),
        password,
        role
      }, token);

      alert('Employee and user account created successfully!');
      setForm({ emp_id: '', name: '', email: '', designation: '', mgr_id: '', password: '', role: 'developer' });
    } catch (err) {
      alert(err.message);
    }
  };

  return (
    <div className="p-6 max-w-2xl mx-auto">
      <h2 className="text-2xl font-bold mb-6">Create Employee</h2>
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow space-y-4">
        {/* All fields: emp_id, name, email, designation, mgr_id (optional), password, role */}
        <button type="submit" className="bg-green-600 text-white py-3 rounded-lg w-full hover:bg-green-700">Create Employee & User</button>
      </form>
    </div>
  );
};

// List / Update / Delete Employees
const ListEmployees = () => {
  const { token } = useAuth();
  const [employees, setEmployees] = useState([]);
  useEffect(() => { apiCall('/api/v1/employees', 'GET', null, token).then(setEmployees); }, [token]);

  const deleteEmp = async (id) => {
    if (window.confirm('Delete this employee?')) {
      await apiCall(`/api/v1/employees/${id}`, 'DELETE', null, token);
      setEmployees(employees.filter(e => e.emp_id !== id));
    }
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-6">Manage Employees</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full bg-white shadow rounded-lg">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left">ID</th>
              <th className="px-6 py-3 text-left">Name</th>
              <th className="px-6 py-3 text-left">Email</th>
              <th className="px-6 py-3 text-left">Designation</th>
              <th className="px-6 py-3 text-left">Manager</th>
              <th className="px-6 py-3 text-left">Actions</th>
            </tr>
          </thead>
          <tbody>
            {employees.map(emp => (
              <tr key={emp.emp_id}>
                <td className="px-6 py-4">{emp.emp_id}</td>
                <td className="px-6 py-4">{emp.name}</td>
                <td className="px-6 py-4">{emp.email}</td>
                <td className="px-6 py-4">{emp.designation}</td>
                <td className="px-6 py-4">{emp.mgr_id || 'None'}</td>
                <td className="px-6 py-4">
                  <button className="text-blue-600 mr-4"><Edit size={18} /></button>
                  <button onClick={() => deleteEmp(emp.emp_id)} className="text-red-600"><Trash2 size={18} /></button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

// Create User
const CreateUser = () => {
  const { token } = useAuth();
  const [form, setForm] = useState({ emp_id: '', password: '', role: 'developer' });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await apiCall('/api/v1/users', 'POST', { ...form, emp_id: parseInt(form.emp_id) }, token);
      alert('User created!');
    } catch (err) { alert(err.message); }
  };

  return (
    <div className="p-6 max-w-md mx-auto">
      <h2 className="text-2xl font-bold mb-6">Create User</h2>
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow space-y-4">
        <input type="number" placeholder="Employee ID" value={form.emp_id} onChange={e => setForm({...form, emp_id: e.target.value})} required className="w-full border rounded px-4 py-2" />
        <input type="password" placeholder="Password" value={form.password} onChange={e => setForm({...form, password: e.target.value})} required className="w-full border rounded px-4 py-2" />
        <select value={form.role} onChange={e => setForm({...form, role: e.target.value})} className="w-full border rounded px-4 py-2">
          <option value="developer">Developer</option>
          <option value="manager">Manager</option>
          <option value="admin">Admin</option>
        </select>
        <button type="submit" className="w-full bg-indigo-600 text-white py-3 rounded hover:bg-indigo-700">Create User</button>
      </form>
    </div>
  );
};

// List Users (Admin Only)
const ListUsers = () => {
  const { token } = useAuth();
  const [users, setUsers] = useState([]);
  useEffect(() => { apiCall('/api/v1/users', 'GET', null, token).then(setUsers); }, [token]);

  const deleteUser = async (emp_id) => {
    if (confirm('Delete user?')) {
      await apiCall(`/api/v1/users/${emp_id}`, 'DELETE', null, token);
      setUsers(users.filter(u => u.emp_id !== emp_id));
    }
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-6">Manage Users</h2>
      <table className="min-w-full bg-white shadow rounded-lg">
        <thead className="bg-gray-50">
          <tr><th className="px-6 py-3 text-left">Emp ID</th><th className="px-6 py-3 text-left">Role</th><th>Actions</th></tr>
        </thead>
        <tbody>
          {users.map(u => (
            <tr key={u.emp_id}>
              <td className="px-6 py-4">{u.emp_id}</td>
              <td className="px-6 py-4">{u.role}</td>
              <td className="px-6 py-4">
                <button className="text-red-600" onClick={() => deleteUser(u.emp_id)}><Trash2 size={18} /></button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

// Main App
function App() {
  return (
    <AuthProvider>
      <MainApp />
    </AuthProvider>
  );
}

const MainApp = () => {
  const { user, loading } = useAuth();

  if (loading) return <div className="flex h-screen items-center justify-center">Loading...</div>;
  if (!user) return <LoginPage />;

  return <Dashboard />;
};

export default App;