import React from 'react';
import { CheckCircle2, Circle } from 'lucide-react';

function StatsCards({ stats }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
      <div className="bg-white rounded-xl shadow-lg p-6 transform hover:scale-105 transition-transform">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-gray-600 text-sm font-medium">Total Tasks</p>
            <p className="text-3xl font-bold text-indigo-600">{stats.total}</p>
          </div>
          <div className="bg-indigo-100 p-3 rounded-full">
            <CheckCircle2 className="text-indigo-600" size={24} />
          </div>
        </div>
      </div>
      
      <div className="bg-white rounded-xl shadow-lg p-6 transform hover:scale-105 transition-transform">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-gray-600 text-sm font-medium">Completed</p>
            <p className="text-3xl font-bold text-green-600">{stats.completed}</p>
          </div>
          <div className="bg-green-100 p-3 rounded-full">
            <CheckCircle2 className="text-green-600" size={24} />
          </div>
        </div>
      </div>
      
      <div className="bg-white rounded-xl shadow-lg p-6 transform hover:scale-105 transition-transform">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-gray-600 text-sm font-medium">Active</p>
            <p className="text-3xl font-bold text-orange-600">{stats.active}</p>
          </div>
          <div className="bg-orange-100 p-3 rounded-full">
            <Circle className="text-orange-600" size={24} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default StatsCards;