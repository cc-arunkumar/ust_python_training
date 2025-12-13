import { useState } from 'react';
import './level3.css'; // Import the CSS you already have

export default function Level3() {
  const [tasks, setTasks] = useState([
    { id: 1, text: 'Learn React useState', completed: false },
    { id: 2, text: 'Build a counter app', completed: false },
    { id: 3, text: 'Complete this challenge', completed: false },
  ]);

  const [employees, setEmployees] = useState([]);
  const [newName, setNewName] = useState('');
  const [newRole, setNewRole] = useState('');

  const items = ['Apple', 'Banana', 'Orange', 'Mango', 'Grape'];
  const [checkedItems, setCheckedItems] = useState([]);

  const toggleComplete = (id) => {
    setTasks(tasks.map(task =>
      task.id === id ? { ...task, completed: !task.completed } : task
    ));
  };

  const addEmployee = () => {
    if (newName.trim() && newRole.trim()) {
      setEmployees([...employees, { id: Date.now(), name: newName.trim(), role: newRole.trim() }]);
      setNewName('');
      setNewRole('');
    }
  };

  const removeEmployee = (id) => {
    setEmployees(employees.filter(emp => emp.id !== id));
  };

  const toggleCheckbox = (item) => {
    setCheckedItems(prev =>
      prev.includes(item) ? prev.filter(i => i !== item) : [...prev, item]
    );
  };

  return (
    <section className="level-section">
      <h2>Level 3: Array/Object State</h2>

      <div className="challenge">
        <h3>Task List (Toggle Complete)</h3>
        <ul className="task-list">
          {tasks.map(task => (
            <li key={task.id} className={task.completed ? 'completed' : ''}>
              {task.text}
              <button onClick={() => toggleComplete(task.id)}>
                {task.completed ? 'Undo' : 'Complete'}
              </button>
            </li>
          ))}
        </ul>
      </div>

      <div className="challenge">
        <h3>Add & Remove Employee</h3>
        <div className="employee-form">
          <input
            type="text"
            placeholder="Name"
            value={newName}
            onChange={(e) => setNewName(e.target.value)}
          />
          <input
            type="text"
            placeholder="Role"
            value={newRole}
            onChange={(e) => setNewRole(e.target.value)}
          />
          <button onClick={addEmployee}>Add Employee</button>
        </div>

        <ul className="employee-list">
          {employees.map(emp => (
            <li key={emp.id}>
              {emp.name} - {emp.role}
              <button onClick={() => removeEmployee(emp.id)}>Remove</button>
            </li>
          ))}
        </ul>
      </div>

      <div className="challenge">
        <h3>Checkbox List</h3>
        <p>Checked items count: {checkedItems.length}</p>
        <ul className="checkbox-list">
          {items.map(item => (
            <li key={item}>
              <label>
                <input
                  type="checkbox"
                  checked={checkedItems.includes(item)}
                  onChange={() => toggleCheckbox(item)}
                />
                {item}
              </label>
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
}