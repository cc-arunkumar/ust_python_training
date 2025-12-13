// Task - React props
// Task Title: A Reusable EmployeeCard

// Component
// Team: Digital Solutions
// Effort: 15 mins

// Goal
// Create a reusable EmployeeCard component to show employee information in the
// dashboard.

// Requirements
// 1. The component should accept these props:
// name
// employeeId
// role
// location
// 2. Display these details inside a clean card layout:
// Light background
// Border
// Padding
// Rounded corners
// 3. Use this EmployeeCard component in two places:
// Employee List Page
// Task - React props 1
// Project Team Page
// 4. Card must be responsive and look consistent.
// Acceptance Criteria
// Props display correctly
// Card layout is clean and aligned
// Component is reusable

// No console warnings or UI issues
// �� Deliverables
// EmployeeCard.jsx
// Usage example in:
// EmployeeList.jsx
// ProjectTeam.jsx
// Task - React props 2

import { useState } from "react";
import GreetingCard from "./GreetingCard";
import "./App.css";
import WeatherCard from "./WeatherCard";
import ProductCard from "./ProductCard";
import Card from "./Card";
import EmployeeList from "./EmployeeList"; 
import ProjectTeam from "./ProjectTeam";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <div>
        {/* <GreetingCard name="Bhargavi" />
        <GreetingCard name="Meena" />
        <GreetingCard name="Shero" /> */}

        {/* <GreetingCard name="RAM" greeting="Namaste" />
        <GreetingCard name="Shyam" greeting="Vanakkam" />
        <GreetingCard name="Bhargavi" greeting="Good Morning" />
        <GreetingCard name="Harsha" greeting="hi pandi" /> */}

        {/* <WeatherCard city="New Delhi" temperature="22°C" />
        <WeatherCard city="Mumbai" temperature="15°C" />
        <WeatherCard city="New York" temperature="25°C" />
        <WeatherCard city="London" temperature="15°C" /> */}

        {/* <ProductCard name="Bhargavi's Book" price={45} rating="5" />
        <ProductCard name="Meena's Watch" price={120} rating="4.5" />
        <ProductCard name="Appa's Shoes" price={75} rating="4.8" />
        <ProductCard name="Sundar's Bag" price={60} rating="4.3" /> */}

        {/* <Card>
            <h2>Times of India News</h2>
            <hr/>
            <p>ISRO successfully launches new sslv rocket today</p>
        </Card>
        <Card>
            <h2>Kabbadi</h2>
            <p>
                "i Play the games"
            </p>
        </Card> */}

        <div className="App">
          <h1>Employee Card</h1>
          <div className="section">
            <h2>Employee List</h2>
            <EmployeeList /> {/* Employee List Section */}
          </div>
          <div className="section">
            <h2>Project Team</h2>
            <ProjectTeam /> {/* Project Team Section */}
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
