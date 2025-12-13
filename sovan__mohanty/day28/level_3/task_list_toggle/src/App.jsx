import { useState } from "react";
import "./App.css";

function App() {
  // Initial list of items
  const items = ["Task A", "Task B", "Task C", "Task D", "Task E"];

  // State: array of checked items
  const [checkedItems, setCheckedItems] = useState([]);

  // Toggle checkbox
  const handleCheck = (item) => {
    if (checkedItems.includes(item)) {
      // remove item if already checked
      setCheckedItems(checkedItems.filter((i) => i !== item));
    } else {
      // add item if not checked
      setCheckedItems([...checkedItems, item]);
    }
  };

  return (
    <div className="App">
      <h1>Checkbox List Example</h1>
      <ul>
        {items.map((item) => (
          <li key={item}>
            <label>
              <input
                type="checkbox"
                checked={checkedItems.includes(item)}
                onChange={() => handleCheck(item)}
              />
              {item}
            </label>
          </li>
        ))}
      </ul>

      {/* Display count */}
      <p>Checked items count: {checkedItems.length}</p>
    </div>
  );
}

export default App;
