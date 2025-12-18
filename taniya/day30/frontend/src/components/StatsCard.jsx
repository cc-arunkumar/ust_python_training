const StatsCard = ({ title, value, icon: Icon, color, borderColor }) => {
  return (
    <div className={`bg-white rounded-xl shadow-sm p-6 border-l-4 ${borderColor} hover:shadow-md transition-shadow`}>
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm text-gray-600 mb-1">{title}</p>
          <p className="text-3xl font-bold text-gray-900">{value}</p>
        </div>
        {Icon && (
          <div className={`w-12 h-12 ${color} rounded-lg flex items-center justify-center`}>
            <Icon className="w-6 h-6 text-white" />
          </div>
        )}
      </div>
    </div>
  );
};

export default StatsCard;