import React, { useState } from 'react';
import './index.css';

function App() {
  return (
    <div className="app-container">
      <h1>React State Challenge</h1>
      
      <h2>Level 1: Basic State</h2>
      <Counter />
      <ToggleMessage />
      <InputMirror />

      <h2>Level 2: Interactive State</h2>

      <CounterWithLimits />
      <VisibilityToggle />

      <h2>Level 3: Array/Object State</h2>
      <TaskListToggle />
    </div>
  );
}

// Level 1: Basic State
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div className="component-container">
      <h3>Counter: {count}</h3>
      <button onClick={() => setCount(count + 1)} className="btn">+</button>
      <button onClick={() => setCount(count - 1)} className="btn">-</button>
    </div>
  );
}

function ToggleMessage() {
  const [isVisible, setIsVisible] = useState(false);

  return (
    <div className="component-container">
      <button onClick={() => setIsVisible(!isVisible)} className="btn">
        Toggle Message
      </button>
      {isVisible && <p>Welcome to UST Dashboard!</p>}
    </div>
  );
}

function InputMirror() {
  const [input, setInput] = useState('');

  return (
    <div className="component-container">
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        className="input"
        placeholder="Type something..."
      />
      <p>You typed: {input}</p>
    </div>
  );
}

// Level 2: Interactive State
function ColorChanger() {
  const [colorIndex, setColorIndex] = useState(0);
  const colors = ["#FF5733", "#33FF57", "#3357FF"];

  return (
    <div className="color-changer" style={{ backgroundColor: colors[colorIndex] }}>
      <button onClick={() => setColorIndex((colorIndex + 1) % colors.length)} className="btn">
        Change Color
      </button>
    </div>
  );
}

function CounterWithLimits() {
  const [count, setCount] = useState(0);

  const increase = () => {
    if (count < 10) {
      setCount(count + 1);
    } else {
      alert("Maximum limit reached!");
    }
  };

  const decrease = () => {
    if (count > 0) {
      setCount(count - 1);
    } else {
      alert("Minimum limit reached!");
    }
  };

  return (
    <div className="component-container">
      <h3>Counter: {count}</h3>
      <button onClick={increase} className="btn">+</button>
      <button onClick={decrease} className="btn">-</button>
    </div>
  );
}

function VisibilityToggle() {
  const [isVisible, setIsVisible] = useState(false);

  return (
    <div className="component-container">
      <button onClick={() => setIsVisible(!isVisible)} className="btn">
        {isVisible ? "Hide Details" : "Show Details"}
      </button>
      {isVisible && <p>Here are the hidden details...</p>}
    </div>
  );
}

// Level 3: Array/Object State
function TaskListToggle() {
  const [tasks, setTasks] = useState([
    { id: 1, text: "Task 1", completed: false },
    { id: 2, text: "Task 2", completed: false },
    { id: 3, text: "Task 3", completed: false },
  ]);

  const toggleTask = (id) => {
    setTasks(tasks.map((task) =>
      task.id === id ? { ...task, completed: !task.completed } : task
    ));
  };

  return (
    <div className="component-container">
      {tasks.map((task) => (
        <div key={task.id}>
          <span style={{ textDecoration: task.completed ? "line-through" : "" }}>
            {task.text}
          </span>
          <button onClick={() => toggleTask(task.id)} className="btn">
            {task.completed ? "Undo" : "Complete"}
          </button>
        </div>
      ))}
    </div>
  );
}

export default App;
