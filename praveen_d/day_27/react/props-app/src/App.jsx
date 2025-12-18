import './App.css'
import Greet from './Greet'
import EmployeeListPage from './EmployeeListPage'
import ProjectTeamPage from './ProjectTeamPage'

function App() {
  // const [count, setCount] = useState(0)

  return (
    <>

    <h1>CARDS</h1>
    <img src='/assets/ChatGPT_Image_Dec_12__2025__01_06_59_PM-removebg-preview'></img>
      <EmployeeListPage name="Kabil" employeeId="A123" role="DEV" location="BANGLORE"/>
      <EmployeeListPage name="Praveen" employeeId="A1234" role="DEV" location="CHENNAI"/>

      <ProjectTeamPage name="Kabil" employeeId="A123" role="DEV" location="BANGLORE"/>
      <ProjectTeamPage name="Praveen" employeeId="A1234" role="DEV" location="CHENNAI"/>

      <EmployeeListPage name="Kabil" employeeId="A123" role="DEV" location="BANGLORE"/>
      <EmployeeListPage name="Praveen" employeeId="A1234" role="DEV" location="CHENNAI"/>
      
      <ProjectTeamPage name="Kabil" employeeId="A123" role="DEV" location="BANGLORE"/>
      <ProjectTeamPage name="Praveen" employeeId="A1234" role="DEV" location="CHENNAI"/>

    </>
  )
}

export default App
