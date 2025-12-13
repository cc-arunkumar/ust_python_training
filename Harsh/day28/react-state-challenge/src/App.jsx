import Counter from "./components/Counter";
import ToggleMessage from "./components/ToggleMessage";
import InputMirror from "./components/InputMirror";
import ColorChanger from "./components/ColorChanger";
import CounterWithLimits from "./components/CounterWithLimits";
import VisibilityToggle from "./components/VisibilityToggle";
import TaskListToggle from "./components/TaskListToggle";
import EmployeeManager from "./components/EmployeeManager";
import CheckboxList from "./components/CheckboxList";
import "./App.css";

function App() {
  return (
    <div className="app-container">
      <h1 className="app-title">React State Challenges</h1>

      <div className="card"><Counter /></div>
      <div className="card"><ToggleMessage /></div>
      <div className="card"><InputMirror /></div>
      <div className="card"><ColorChanger /></div>
      <div className="card"><CounterWithLimits /></div>
      <div className="card"><VisibilityToggle /></div>
      <div className="card"><TaskListToggle /></div>
      <div className="card"><EmployeeManager /></div>
      <div className="card"><CheckboxList /></div>
    </div>
  );
}

export default App;
