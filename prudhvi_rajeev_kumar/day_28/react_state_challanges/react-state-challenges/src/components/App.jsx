import "./App.css";
import Counter from "./Level1/Counter.jsx";
import ToggleMessage from "./Level1/ToggleMessage.jsx";
import InputMirror from "./Level1/InputMirror.jsx";
import ColorChanger from "./Level2/ColorChanger.jsx";
import LimitedCounter from "./Level2/LimitedCounter.jsx";
import VisibilityToggle from "./Level2/VisibilityToggle.jsx";
import TaskList from "./Level3/TaskList.jsx";
import EmployeeList from "./Level3/EmployeeList.jsx";
import EmployeeListWithRemove from "./Level3/EmployeeListWithRemove.jsx";
import CheckboxList from "./Level3/CheckboxList.jsx";

export default function App() {
  return (
    <main className="container">
      <h1>React State Challenges</h1>

      <div className="grid">
        <Counter />
        <ToggleMessage />
        <InputMirror />
        <ColorChanger />
        <LimitedCounter />
        <VisibilityToggle />
        <TaskList />
        <EmployeeList />
        <EmployeeListWithRemove />
        <CheckboxList />
      </div>
    </main>
  );
}
