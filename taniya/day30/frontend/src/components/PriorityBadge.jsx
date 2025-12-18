const PriorityBadge = ({ priority }) => {
  const colors = {
    HIGH: 'bg-red-100 text-red-700 border-red-200',
    MEDIUM: 'bg-yellow-100 text-yellow-700 border-yellow-200',
    LOW: 'bg-green-100 text-green-700 border-green-200'
  };
  return (
    <span className={`px-2 py-1 rounded-full text-xs font-medium border ${colors[priority]}`}>
      {priority}
    </span>
  );
};

export default PriorityBadge;