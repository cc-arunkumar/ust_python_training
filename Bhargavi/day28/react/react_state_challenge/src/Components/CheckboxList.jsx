import React, { useState } from "react";

function CheckboxList() {
  const [checkedItems, setCheckedItems] = useState([]);

  const handleCheckboxChange = (event) => {
    const value = event.target.value;
    setCheckedItems((prev) =>
      prev.includes(value)
        ? prev.filter((item) => item !== value)
        : [...prev, value]
    );
  };

  return (
    <div className="box">
      <ul>
        {["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"].map((item) => (
          <li key={item}>
            <input
              type="checkbox"
              value={item}
              onChange={handleCheckboxChange}
            />
            {item}
          </li>
        ))}
      </ul>
      <p>Checked Items: {checkedItems.length}</p>
    </div>
  );
}

export default CheckboxList;
