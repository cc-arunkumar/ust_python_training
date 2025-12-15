import { useState } from "react";

export default function CheckboxList() {
  const items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"];
  const [checkedItems, setCheckedItems] = useState([]);

  const toggle = (item) => {
    setCheckedItems(prev =>
      prev.includes(item) ? prev.filter(i => i !== item) : [...prev, item]
    );
  };

  return (
    <section className="card">
      <h3>Checkbox List</h3>
      {items.map(item => (
        <label key={item} className="row">
          <input
            type="checkbox"
            checked={checkedItems.includes(item)}
            onChange={() => toggle(item)}
          />
          <span>{item}</span>
        </label>
      ))}
      <p>Checked items: {checkedItems.length}</p>
    </section>
  );
}
