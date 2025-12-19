// src/pages/CreateTask.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useAuth } from '../context/AuthContext';

const CreateTask = () => {
  const { user } = useAuth();
  const [employees, setEmployees] = useState([]);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');

  const [formData, setFormData] = useState({
    title: '',
    description: '',
    assigned_to: '',
    priority: 'medium',
    status: 'pending',
    reviewer: '',
    expected_closure: '',
    remarks: '',
    created_by: user?.emp_id || '',
    assigned_by: user?.emp_id || '',
  });

  useEffect(() => {
    // Fetch employees for dropdowns
    axios.get('/api/v1/employees')
      .then(res => setEmployees(res.data))
      .catch(() => setError('Failed to load employees'));
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess('');

    try {
      // Format date properly
      const payload = {
        ...formData,
        expected_closure: new Date(formData.expected_closure).toISOString(),
        priority: formData.priority.toLowerCase(),
        status: formData.status.toLowerCase(),
      };

      await axios.post('/api/v1/tasks', payload);
      setSuccess('Task created successfully!');
      // Reset form or redirect
    } catch (err) {
      if (err.response?.status === 400) {
        setError(err.response.data.detail || 'Reviewer must be a manager');
      } else if (err.response?.status === 422) {
        const details = err.response.data.detail;
        const msg = details.map(d => `${d.loc.join(' → ')}: ${d.msg}`).join('; ');
        setError('Validation error: ' + msg);
      } else {
        setError('Failed to create task');
      }
    }
  };

  if (!user) return <div>Loading...</div>;

  return (
    <div className="max-w-2xl mx-auto p-6">
      <h2 className="text-2xl font-bold mb-6">Create New Task</h2>
      
      {error && <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">{error}</div>}
      {success && <div className="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded mb-4">{success}</div>}

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block font-medium">Title</label>
          <input name="title" value={formData.title} onChange={handleChange} required className="w-full p-2 border rounded" />
        </div>

        <div>
          <label className="block font-medium">Description</label>
          <textarea name="description" value={formData.description} onChange={handleChange} required className="w-full p-2 border rounded" rows="4" />
        </div>

        <div>
          <label className="block font-medium">Assign To</label>
          <select name="assigned_to" value={formData.assigned_to} onChange={handleChange} required className="w-full p-2 border rounded">
            <option value="">Select Employee</option>
            {employees.map(emp => (
              <option key={emp.emp_id} value={emp.emp_id}>
                {emp.name} ({emp.emp_id}) - {emp.designation}
              </option>
            ))}
          </select>
        </div>

        <div>
          <label className="block font-medium">Reviewer (Must be Manager)</label>
          <select name="reviewer" value={formData.reviewer} onChange={handleChange} required className="w-full p-2 border rounded">
            <option value="">Select Manager</option>
            {employees
              .filter(emp => emp.mgr_id === null) // Managers have mgr_id = None
              .map(emp => (
                <option key={emp.emp_id} value={emp.emp_id}>
                  {emp.name} ({emp.emp_id}) - {emp.designation}
                </option>
              ))}
          </select>
        </div>

        <div>
          <label className="block font-medium">Priority</label>
          <select name="priority" value={formData.priority} onChange={handleChange} className="w-full p-2 border rounded">
            <option value="high">High</option>
            <option value="medium">Medium</option>
            <option value="low">Low</option>
          </select>
        </div>

        <div>
          <label className="block font-medium">Expected Closure</label>
          <input type="date" name="expected_closure" value={formData.expected_closure} onChange={handleChange} required className="w-full p-2 border rounded" />
        </div>

        <div>
          <label className="block font-medium">Remarks (Optional)</label>
          <textarea name="remarks" value={formData.remarks} onChange={handleChange} className="w-full p-2 border rounded" />
        </div>

        <button type="submit" className="bg-blue-600 text-white px-6 py-3 rounded hover:bg-blue-700">
          Create Task
        </button>
      </form>
    </div>
  );
};

export default CreateTask;