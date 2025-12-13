import EmployeeCard from "./EmployeeCard.jsx";
import srkImage from './assets/srk.webp';
const EmployeeList = () => {
  return (
    <div>
      <h2 >Employees list</h2>
      <EmployeeCard name ="Niranjan" employeeId={101} role="SDE" location="Hyderabad" image={srkImage} />
      <EmployeeCard name ="sai" employeeId={102} role="SDE" location="Chennai" image={srkImage}/>
      <EmployeeCard name ="Vikash" employeeId={103} role="IT" location="Bengalore" image={srkImage}/>

      <EmployeeCard name ="Vamshi" employeeId={104} role="SDE" location="Chennai" image={srkImage}/>
      
    </div>
  );
};

export default EmployeeList;
