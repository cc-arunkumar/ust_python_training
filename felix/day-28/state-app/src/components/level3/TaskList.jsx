import { useState } from 'react';
import './TaskList.css'

export default function TaskList() {
  const [tasks, setTasks] = useState([
    { id: 1, text: 'Review dashboard metrics', completed: false },
    { id: 2, text: 'Update client reports', completed: false },
    { id: 3, text: 'Team meeting preparation', completed: false }
  ]);

  const toggleTask = (id) => {
    setTasks(tasks.map(task => 
      task.id === id ? { ...task, completed: !task.completed } : task
    ));
  };

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="font-semibold text-lg mb-3 text-slate-700">1. Task List Toggle</h3>
      <ul className="space-y-2">
        {tasks.map(task => (
          <li 
            key={task.id} 
            className="flex items-center justify-between bg-slate-50 p-3 rounded"
          >
            <span className={task.completed ? 'line-through text-slate-400' : 'text-slate-700'}>
              {task.text}
            </span>
            <button 
              onClick={() => toggleTask(task.id)}
              className={`px-3 py-1 rounded text-sm ${
                task.completed 
                  ? 'bg-slate-300 text-slate-600' 
                  : 'bg-green-500 text-white hover:bg-green-600'
              }`}
            >
              {task.completed ? 'Undo' : 'Complete'}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}