import { useState } from 'react';
import './VisibilityToggle.css'

export default function VisibilityToggle() {
  const [showDetails, setShowDetails] = useState(false);

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="font-semibold text-lg mb-3 text-slate-700">3. Visibility Toggle</h3>
      <button 
        onClick={() => setShowDetails(!showDetails)} 
        className="w-full bg-indigo-500 text-white py-2 rounded hover:bg-indigo-600 mb-3"
      >
        {showDetails ? 'Hide' : 'Show'} Details
      </button>
      {showDetails && (
        <div className="bg-indigo-50 border border-indigo-200 p-4 rounded text-slate-700">
          <p className="font-medium mb-2">Additional Information</p>
          <p className="text-sm">
            This component demonstrates conditional rendering using React state. 
            Toggle the button to show or hide content dynamically.
          </p>
        </div>
      )}
    </div>
  );
}