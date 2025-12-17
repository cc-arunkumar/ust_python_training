import React from 'react';
import { AlertCircle, Clock, CheckCircle } from 'lucide-react';
import TaskCard from './TaskCard';
import { TASK_STATUS } from '../../utils/constants';

const TasksBoard = ({ tasks, onStatusChange, canEdit }) => {
  const todoTasks = tasks.filter(t => t.status === TASK_STATUS.TODO);
  const inProgressTasks = tasks.filter(t => t.status === TASK_STATUS.IN_PROGRESS);
  const completedTasks = tasks.filter(t => t.status === TASK_STATUS.COMPLETED);

  const Column = ({ title, tasks, icon: Icon, color, count }) => (
    <div className="flex-1 min-w-[300px]">
      <div className={`${color} rounded-lg p-4 mb-4 shadow-md`}>
        <div className="flex items-center gap-2 text-white">
          <Icon className="w-5 h-5" />
          <h2 className="font-semibold text-lg">{title}</h2>
          <span className="ml-auto bg-white bg-opacity-30 px-3 py-1 rounded-full text-sm font-medium">
            {count}
          </span>
        </div>
      </div>
      
      <div className="space-y-3 min-h-[200px]">
        {tasks.length === 0 ? (
          <div className="text-center py-12 text-gray-400 bg-gray-50 rounded-lg border-2 border-dashed border-gray-200">
            <p className="text-sm">No tasks in this column</p>
          </div>
        ) : (
          tasks.map(task => (
            <TaskCard
              key={task._id}
              task={task}
              onStatusChange={onStatusChange}
              canEdit={canEdit}
            />
          ))
        )}
      </div>
    </div>
  );

  return (
    <div className="flex gap-6 overflow-x-auto pb-4">
      <Column
        title="To Do"
        tasks={todoTasks}
        icon={AlertCircle}
        color="bg-gradient-to-r from-red-500 to-pink-500"
        count={todoTasks.length}
      />
      <Column
        title="In Progress"
        tasks={inProgressTasks}
        icon={Clock}
        color="bg-gradient-to-r from-yellow-500 to-orange-500"
        count={inProgressTasks.length}
      />
      <Column
        title="Completed"
        tasks={completedTasks}
        icon={CheckCircle}
        color="bg-gradient-to-r from-green-500 to-teal-500"
        count={completedTasks.length}
      />
    </div>
  );
};

export default TasksBoard;