import React, { useState } from 'react';

const CheckboxList = () => {
  const [checkedItems, setCheckedItems] = useState([]);

  const handleCheckboxChange = (item) => {
    setCheckedItems((prevState) =>
      prevState.includes(item)
        ? prevState.filter((i) => i !== item)
        : [...prevState, item]
    );
  };

  const items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5'];

  return (
    <div>
      {items.map((item, index) => (
        <div key={index}>
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
