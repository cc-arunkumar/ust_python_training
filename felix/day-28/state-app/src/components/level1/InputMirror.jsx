import { useState } from 'react';
import "./InputMirror.css"

export default function InputMirror() {
  const [inputText, setInputText] = useState('');

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="font-semibold text-lg mb-3 text-slate-700">3. Input Mirror</h3>
      <input 
        type="text" 
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Type something..."
        className="w-full border border-slate-300 rounded px-3 py-2 mb-3"
      />
      <div className="bg-slate-50 p-3 rounded min-h-[40px] text-slate-700">
        {inputText || <span className="text-slate-400">Your text will appear here...</span>}
      </div>
    </div>
  );
}