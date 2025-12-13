import { useState } from "react";
import "./App.css";

function App() {
  // state to track visibility
  const [showDetails, setShowDetails] = useState(false);

  return (
    <div className="App">
      <h1>Visibility Toggle Example</h1>

      {/* Toggle button */}
      <button onClick={() => setShowDetails(!showDetails)}>
        {showDetails ? "Hide Details" : "Show Details"}
      </button>

      {/* Conditional rendering */}
      {showDetails && (
        <div className="details">
          <p>Welcome to UST Dashboard! Here are some hidden details revealed on toggle.</p>
        </div>
      )}
    </div>
  );
}

export default App;
