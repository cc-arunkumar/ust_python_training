import { useState } from 'react';

export default function ColorChanger() {
  const colors = ['bg-blue-400', 'bg-green-400', 'bg-purple-400', 'bg-pink-400'];
  const [colorIndex, setColorIndex] = useState(0);

  const changeColor = () => {
    setColorIndex((colorIndex + 1) % colors.length);
  };

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="font-semibold text-lg mb-3 text-slate-700">1. Color Changer</h3>
      <div className={`${colors[colorIndex]} h-32 rounded mb-3 transition-colors duration-300`}></div>
      <button 
        onClick={changeColor} 
        className="w-full bg-slate-700 text-white py-2 rounded hover:bg-slate-800"
      >
        Change Color
      </button>
    </div>
  );
}