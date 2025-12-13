import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import GreetCard from "./GreetingCard";
import WhetherCard from "./WhetherCard";
import ProductCard from "./ProductCard";
import Card from "./Card";
import EmployeeCard from "./EmployeeCard";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <h1>Hey There.....</h1>
      {/*<div className="left-side">
        <GreetCard name="RAM" text="Namaste" />
      </div>
      <div className="right-side">
        <GreetCard name="Shyam" text="Vanakkam" />
      </div>
      <div className="left-side">
        <GreetCard name="Varsha" text="Cheeeeee...." />
      </div>
      <div className="right-side">
        <GreetCard name="Yeshu" text="Hii....Helloo...." />
      </div> */}
      {/* <div className="left-side">
        <WhetherCard name="New Delhi" temparature={21} />
      </div>
      <div className="right-side">
        <WhetherCard name="Mumbai" temparature={22} />
      </div>
      <div className="left-side">
        <WhetherCard name="Kolkata" temparature={23} />
      </div>
      <div className="right-side">
        <WhetherCard name="Chennai" temparature={24} />
      </div> */}
      {/* <div className = "left-side">
        <ProductCard name = "Smartphone" price = {21} rating = {4.3} />
      </div>
      <div className="right-side">
        <ProductCard name = "Laptop" price = {22} rating = {4.5}/>
      </div>
      <div className="left-side">
        <ProductCard name = "Headphones" price = {23} rating = {4.6}/>
      </div>
      <div className="right-side">
        <ProductCard name = "Smartwatch" price = {24} rating = {4.8}/>
      </div> */}
      {/* <Card>
        <div className="child">
          <h2>Times of India News</h2>
          <hr />
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
        </div>
      </Card>
      <Card>
        <div className="child">
          <h2>Sports News</h2>
          <hr />
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
        </div>
      </Card> */}
      <div className="employeecard">
        <EmployeeCard image_url = "./pexels-moh-adbelghaffar-771742.jpg" name = "Felix" employeeId = "U1011" role = "SDE-1" location = "Kottayam"/>
        </div>
        <div className="employeecard">
        <EmployeeCard image_url = "./pexels-lakshya-sanwal-1663958966-28841514.jpg" name = "Arun" employeeId = "U1012" role = "SDE-2" location = "Trivandrun"/>
        </div>
        <div className="employeecard">
        <EmployeeCard image_url = "./pexels-jibarofoto-1759530.jpg" name = "Akhil" employeeId = "U1012" role = "SDE-3" location = "Kollam"/>
      </div>
    </>
  );
}
export default App;