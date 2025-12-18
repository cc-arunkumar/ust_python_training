import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import Level1 from "./components/Level1";
import Level2 from "./components/Level2";
import Level3 from "./components/Level3";

function App() {
  return (
    <>
      <div>
        <h1>Level1</h1>
        <div className="level_container">
          <Level1 />
        </div>
        <h1>Level2</h1>
        <div className="level_container">
          <Level2 />
        </div>
        <h1>Level3</h1>
        <div className="level_container">
          <Level3 />
        </div>
      </div>
    </>
  );
}

export default App;
