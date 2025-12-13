
const EmployeeCard = ({ name, employeeId, role,location,image } = { ...props }) => {
  return (
    <div className="card" >
      <img src={image} alt={`${name}'s photo`} style={{ width: "100px", height: "100px", borderRadius: "50%" }} />
      <h1>{name}</h1>
      <h3>Employee ID: {employeeId}</h3>
      <h3>Role: {role}</h3>
      <h3>Location: {location}</h3>

    </div>
  );
};

export default EmployeeCard;
