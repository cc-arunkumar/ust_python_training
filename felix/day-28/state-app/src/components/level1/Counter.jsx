import { useState } from 'react';
import './Counter.css'

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="font-semibold text-lg mb-3 text-slate-700">1. Counter</h3>
      <div className="text-4xl font-bold text-center my-4 text-blue-600">
        {count}
      </div>
      <div className="flex gap-2">
        <button 
          onClick={() => setCount(count - 1)} 
          className="flex-1 bg-red-500 text-white py-2 rounded hover:bg-red-600"
        >
          -
        </button>
        <button 
          onClick={() => setCount(count + 1)} 
          className="flex-1 bg-green-500 text-white py-2 rounded hover:bg-green-600"
        >
          +
        </button>
      </div>
    </div>
  );
}