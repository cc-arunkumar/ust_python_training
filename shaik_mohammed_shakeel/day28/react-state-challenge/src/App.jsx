// Import necessary hooks and components
import { useState } from "react"; // useState is a React hook for managing state
import reactLogo from "./assets/react.svg"; // Importing React logo
import viteLogo from "/vite.svg"; // Importing Vite logo (assuming you're using Vite for the project)
import "./App.css"; // Importing the main CSS file for styling
import Basic from "./Basic"; // Importing the Basic component
import Intermediate from "./Intermediate"; // Importing the Intermediate component
import Array from "./Array.jsx"; // Importing the Array component (jsx file extension)

// App component
function App() {
  // State variable for managing a count (not currently used in the component)
  const [count, setCount] = useState(0);

  // Render the components: Basic, Intermediate, and Array
  return (
    <>
      <Basic /> {/* Render the Basic component */}
      <Intermediate /> {/* Render the Intermediate component */}
      <Array /> {/* Render the Array component */}
    </>
  );
}

// Export the App component as default for use in other files
export default App;
