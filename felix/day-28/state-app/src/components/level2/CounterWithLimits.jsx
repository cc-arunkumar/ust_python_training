import { useState } from 'react';
import './CounterWithLimits.css'

export default function CounterWithLimits() {
  const [count, setCount] = useState(0);

  const handleIncrement = () => {
    if (count >= 10) {
      alert('Limit reached! Maximum value is 10');
      return;
    }
    setCount(count + 1);
  };

  const handleDecrement = () => {
    if (count <= 0) {
      alert('Limit reached! Minimum value is 0');
      return;
    }
    setCount(count - 1);
  };

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="font-semibold text-lg mb-3 text-slate-700">2. Counter with Limits</h3>
      <div className="text-4xl font-bold text-center my-4 text-purple-600">
        {count}
      </div>
      <div className="text-center text-sm text-slate-500 mb-3">Min: 0 | Max: 10</div>
      <div className="flex gap-2">
        <button 
          onClick={handleDecrement} 
          className="flex-1 bg-red-500 text-white py-2 rounded hover:bg-red-600"
        >
          -
        </button>
        <button 
          onClick={handleIncrement} 
          className="flex-1 bg-green-500 text-white py-2 rounded hover:bg-green-600"
        >
          +
        </button>
      </div>
    </div>
  );
}