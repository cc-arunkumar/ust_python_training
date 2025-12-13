import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import GreetingCard from "./GrettingCard.jsx";
import WeatherCard from "./WeatherCard.jsx";

import ProductCard from "./ProductCard.jsx";
import Card from "./Card.jsx";

function App() {

  return (
    <>
      <Card>
        <h1>Hello Guys</h1>
        <p>Lorem ipsum dolor sit amet.</p>
      </Card>

      <Card>
        <h1>Sports club</h1>
        <p>You can play cricket and football </p>
      </Card>

      {/* <h1>Welcome to product list</h1>
      <ProductCard name="Phone" price={42000} rating={4.5} />
      <ProductCard name="Car" price={420000} rating={3.5} />
      <ProductCard name="Bike" price={12000} rating={4.5} />
      <ProductCard name="Watch" price={22000} rating={2.5} />
       
      <WeatherCard city="Hyderabad" temprature={22} />
      <WeatherCard city="Mumbai" temprature={23} />
      <WeatherCard city="Kolkata" temprature={22} />
      <WeatherCard city="Chennai" temprature={22} />

    
      <GreetingCard name="Niranjan" greet="Namaste" />
      <GreetingCard name="Sai" greet="Vanakkam" />
      <GreetingCard name="Abhi" greet="Namaste" />
      <GreetingCard name="Sunku" greet="Vanakkam" />  */}
    </>
  );
}

export default App;
