import EmployeeCard from "./EmployeeCard.jsx";
import srkImage from './assets/srk.webp'
const ProjectTeam = () => {
  return (
    <div>
      <h2>Project Team</h2>
      <EmployeeCard name ="Arun" employeeId={105} role="SDE" location="Hyderabad" image={srkImage}/>
      <EmployeeCard name ="Abhi" employeeId={106} role="SDE" location="Chennai" image={srkImage}/>
      <EmployeeCard name ="Shakeel" employeeId={107} role="SDE" location="Chennai" image={srkImage}/>
      <EmployeeCard name ="Anjan" employeeId={108} role="SDE" location="Chennai" image={srkImage}/>

      
    </div>
  );
};

export default ProjectTeam;
