import { CheckCircle2, Circle, Clock, AlertCircle } from 'lucide-react';

const TaskStatusIcon = ({ status }) => {
  switch (status) {
    case 'TO_DO':
      return <Circle className="w-5 h-5 text-gray-400" />;
    case 'IN_PROGRESS':
      return <Clock className="w-5 h-5 text-blue-500" />;
    case 'REVIEW':
      return <AlertCircle className="w-5 h-5 text-yellow-500" />;
    case 'DONE':
      return <CheckCircle2 className="w-5 h-5 text-green-500" />;
    default:
      return <Circle className="w-5 h-5 text-gray-400" />;
  }
};

export default TaskStatusIcon;