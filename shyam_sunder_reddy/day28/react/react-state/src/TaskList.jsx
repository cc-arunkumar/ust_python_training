import { useState } from "react";
function TaskList() {
  const [tasks, setTasks] = useState([
    { id: 1, text: "Task 1", done: false },
    { id: 2, text: "Task 2", done: false },
    { id: 3, text: "Task 3", done: false },
  ]);

  const toggleTask = (id) => {
    setTasks(tasks.map(task =>
      task.id === id ? { ...task, done: !task.done } : task
    ));
  };

  return (
    <ul>
      {tasks.map(task => (
        <li key={task.id} style={{ textDecoration: task.done ? "line-through" : "none" }}>
          {task.text}
          <button onClick={() => toggleTask(task.id)}>Complete</button>
        </li>
      ))}
    </ul>
  );
}

export default TaskList