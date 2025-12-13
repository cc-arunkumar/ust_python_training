import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import GreetingCard from "./GreetingCard";
import Temprature from "./Temprature";
import ProdectCard from "./ProdectCard";
import Card from "./Card";

function App() {
  const [count, setCount] = useState(0);

  return (
    // <>
    //   <GreetingCard name="sai" great="Namaste"/>
    //   <GreetingCard name="vamshi" great="vanakkam"/>
    //   <GreetingCard name="niranjan" great="Namaste"/>
    // </>
    // <>
    //   <Temprature city="Bangalore" weather={22} />
    //   <Temprature city="Trivandram" weather={47} />
    // </>
    <>
    {/* <ProdectCard name="kitkat" cost={10} rating={4.5}/>
    <ProdectCard name="pepsi" cost={30} rating={4.0}/>
    <ProdectCard name="dairy milk" cost={90} rating={5.0}/> */}
<Card>
  <h2>Times of India News</h2>
  <p>Can’t leave manufacturing to China, Rahul tells Indians in US</p>
</Card>
<Card>
  <h2>Sports News</h2>
  <p>
    Malaysian all-rounder becomes only from Associate nation to make IPL 2026 auction final list
  </p>
</Card>
    </>
  );
}

export default App;
