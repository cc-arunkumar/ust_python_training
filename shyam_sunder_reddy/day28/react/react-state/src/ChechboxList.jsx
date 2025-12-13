import { useState } from "react";
function CheckboxList() {
  const items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"];
  const [checked, setChecked] = useState([]);

  const toggleCheck = (item) => {
    setChecked(
      checked.includes(item)
        ? checked.filter(i => i !== item)
        : [...checked, item]
    );
  };

  return (
    <div>
      {items.map(item => (
        <div key={item}>
          <input 
            type="checkbox" 
            checked={checked.includes(item)} 
            onChange={() => toggleCheck(item)} 
          />
          {item}
        </div>
      ))}
      <p>Checked items: {checked.length}</p>
    </div>
  );
}

export default CheckboxList