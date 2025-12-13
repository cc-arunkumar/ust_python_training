import { useState } from 'react';
import './CheckboxList.css'

export default function CheckboxList() {
  const items = ['Analytics', 'Reports', 'Dashboard', 'Settings', 'Profile'];
  const [checkedItems, setCheckedItems] = useState([]);

  const toggleCheckbox = (item) => {
    setCheckedItems(prev => 
      prev.includes(item) 
        ? prev.filter(i => i !== item) 
        : [...prev, item]
    );
  };

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="font-semibold text-lg mb-3 text-slate-700">4. Checkbox List</h3>
      <div className="grid grid-cols-2 md:grid-cols-5 gap-3 mb-4">
        {items.map(item => (
          <label 
            key={item} 
            className="flex items-center space-x-2 cursor-pointer bg-slate-50 p-3 rounded hover:bg-slate-100"
          >
            <input 
              type="checkbox"
              checked={checkedItems.includes(item)}
              onChange={() => toggleCheckbox(item)}
              className="w-4 h-4"
            />
            <span className="text-slate-700">{item}</span>
          </label>
        ))}
      </div>
      <div className="bg-blue-50 border border-blue-200 p-3 rounded text-center">
        <span className="font-semibold text-blue-700">
          Checked Items: {checkedItems.length}
        </span>
        {checkedItems.length > 0 && (
          <div className="text-sm text-blue-600 mt-1">
            {checkedItems.join(', ')}
          </div>
        )}
      </div>
    </div>
  );
}