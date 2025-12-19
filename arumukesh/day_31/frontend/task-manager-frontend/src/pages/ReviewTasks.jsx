// src/pages/ReviewTasks.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useAuth } from '../context/AuthContext';

const ReviewTasks = () => {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);
  const { user } = useAuth();

  useEffect(() => {
    if (!user) return;

    const fetchReviewTasks = async () => {
      try {
        const response = await axios.get('/api/v1/tasks');
        // Filter tasks where current user is the reviewer
        const reviewTasks = response.data.filter(task => task.reviewer === String(user.emp_id));
        setTasks(reviewTasks);
      } catch (err) {
        setError('Failed to fetch review tasks');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchReviewTasks();
  }, [user]);

  if (!user) {
    return <div className="p-6">Loading user information...</div>;
  }

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-6">Tasks to Review</h2>

      {loading && <p className="text-gray-600">Loading tasks...</p>}
      {error && <p className="text-red-600">{error}</p>}

      {!loading && tasks.length === 0 && !error && (
        <div className="bg-yellow-100 border border-yellow-400 text-yellow-700 px-4 py-3 rounded">
          No tasks assigned for review yet.
        </div>
      )}

      {tasks.length > 0 && (
        <div className="overflow-x-auto">
          <table className="min-w-full bg-white border border-gray-200">
            <thead className="bg-gray-100">
              <tr>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">ID</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">Title</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">Status</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">Priority</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">Assignee</th>
                <th className="px-6 py-3 text-left text-xs font-medium text-gray-700 uppercase tracking-wider">Expected Closure</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200">
              {tasks.map(task => (
                <tr key={task.t_id} className="hover:bg-gray-50">
                  <td className="px-6 py-4 whitespace-nowrap">{task.t_id}</td>
                  <td className="px-6 py-4">{task.title}</td>
                  <td className="px-6 py-4">{task.status}</td>
                  <td className="px-6 py-4">{task.priority}</td>
                  <td className="px-6 py-4">{task.assigned_to}</td>
                  <td className="px-6 py-4">{new Date(task.expected_closure).toLocaleDateString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default ReviewTasks;