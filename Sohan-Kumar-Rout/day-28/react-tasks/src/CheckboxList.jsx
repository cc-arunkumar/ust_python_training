import { useState } from "react";

export default function CheckboxList() {
  const items = ["Item A", "Item B", "Item C", "Item D", "Item E"];
  const [checked, setChecked] = useState([]);

  const toggleCheck = (item) => {
    setChecked(prev =>
      prev.includes(item)
        ? prev.filter(i => i !== item)
        : [...prev, item]
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

      <p>Checked: {checked.length}</p>
    </div>
  );
}
