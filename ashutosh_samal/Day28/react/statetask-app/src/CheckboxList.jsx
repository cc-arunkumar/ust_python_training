import React, { useState } from "react";

const CheckboxList = () => {
  const [checkedItems, setCheckedItems] = useState([]);
  const items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"];

  const handleCheckboxChange = (item) => {
    setCheckedItems((prev) =>
      prev.includes(item) ? prev.filter((i) => i !== item) : [...prev, item]
    );
  };

  return (
    <div>
      {items.map((item) => (
        <div key={item}>
          <input
            type="checkbox"
            onChange={() => handleCheckboxChange(item)}
          />
          {item}
        </div>
      ))}
      <p>Checked items count: {checkedItems.length}</p>
    </div>
  );
};

export default CheckboxList;
