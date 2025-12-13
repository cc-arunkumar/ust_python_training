import { useState } from "react";

export default function CheckboxList() {
  const [items, setItems] = useState([
    { id: 1, text: "Learn React", checked: false },
    { id: 2, text: "Master JavaScript", checked: false },
    { id: 3, text: "Build Projects", checked: false },
    { id: 4, text: "Practice Daily", checked: false },
    { id: 5, text: "Read Documentation", checked: false },
  ]);

  const toggleItem = (id) => {
    setItems(
      items.map((item) =>
        item.id === id ? { ...item, checked: !item.checked } : item
      )
    );
  };

  const checkedCount = items.filter((item) => item.checked).length;

  return (
    <div className="checkbox-list-container">
      <div className="checkbox-list-card">
        <h2 className="checkbox-list-title">My Goals</h2>

        <ul className="checkbox-list">
          {items.map((item) => (
            <li key={item.id} className="checkbox-item">
              <label className="checkbox-label">
                <input
                  type="checkbox"
                  checked={item.checked}
                  onChange={() => toggleItem(item.id)}
                  className="checkbox-input"
                />
                <span
                  className={
                    item.checked ? "checkbox-text checked" : "checkbox-text"
                  }
                >
                  {item.text}
                </span>
              </label>
            </li>
          ))}
        </ul>

        <div className="checkbox-count">
          Checked Items: {checkedCount} / {items.length}
        </div>
      </div>
    </div>
  );
}
