import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import EmployeeList from "./EmployeeList.jsx";
import ProjectTeam from "./ProjectTeam.jsx";
import Image from './assets/ust.webp'

function App() {
  return (
    <>
      
      <h1 ><img src={Image} alt={` photo missing`} style={{ width: "100px", height: "100px", marginRight: "2000px" ,marginTop:"-40px" }} />        Employee Dashboard</h1>

      <EmployeeList />
      <ProjectTeam />
    </>
  );
}

export default App;
