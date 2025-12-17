import React from 'react';
import { Mail, Briefcase, Hash } from 'lucide-react';
import { getInitials } from '../../utils/helpers';

const EmployeeCard = ({ employee }) => {
  const colors = [
    'from-blue-400 to-purple-500',
    'from-green-400 to-teal-500',
    'from-orange-400 to-red-500',
    'from-pink-400 to-purple-500',
    'from-indigo-400 to-blue-500'
  ];
  
  const colorIndex = employee.id % colors.length;
  const gradient = colors[colorIndex];

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-5 hover:shadow-lg transition-all">
      <div className="flex items-start gap-4">
        <div className={`w-14 h-14 bg-gradient-to-br ${gradient} rounded-full flex items-center justify-center text-white font-bold text-lg shadow-md flex-shrink-0`}>
          {getInitials(employee.name)}
        </div>
        
        <div className="flex-1 min-w-0">
          <h3 className="font-semibold text-gray-800 text-lg mb-1 truncate">
            {employee.name}
          </h3>
          
          <div className="space-y-1.5">
            <div className="flex items-center gap-2 text-sm text-gray-600">
              <Briefcase className="w-4 h-4 flex-shrink-0" />
              <span className="truncate">{employee.designation}</span>
            </div>
            
            <div className="flex items-center gap-2 text-sm text-gray-600">
              <Mail className="w-4 h-4 flex-shrink-0" />
              <span className="truncate">{employee.email}</span>
            </div>
            
            <div className="flex items-center gap-2 text-xs text-gray-500">
              <Hash className="w-3 h-3 flex-shrink-0" />
              <span>Employee ID: {employee.id}</span>
            </div>

            {employee.manager_id && (
              <div className="flex items-center gap-2 text-xs text-gray-500">
                <span>Manager ID: {employee.manager_id}</span>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default EmployeeCard;