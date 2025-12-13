import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
// import GreetingCard from './GreetingCard'
import Weathercard from './Weathercard.jsx'
import ProductCard from './ProductCard.jsx'
import Card from './Card.jsx'
import EmployeeCard from './EmployeeCard.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      {/* <GreetingCard name="Shakeel" and greet="namaste"/>
      <GreetingCard name="Sai"and greet="namaste"/>
      <GreetingCard name="abhi"and greet="namaste"/> */}
   
      {/* <Weathercard city="New Delhi"  temp={25}/>
      <Weathercard city="Mumbai"  temp={25}/>
      <Weathercard city="Chennai" temp={25}/> */}

      {/* <ProductCard name="BMW" price={200000000} rating={4.8} />
      <ProductCard name="Fortuner" price={6000000} rating={4.5} />
      <ProductCard name="Tharr" price={2000000} rating={4.2} /> */}

      {/* <Card>
        <h2>Times of india</h2>
        <p>A Young Polician won the assembly elections with wooping 90k+ majority </p>
      </Card>
       <card>
        <h2>The Hindu</h2>
        <p>Life story of Young Politician  </p>
      </card> */}

      <EmployeeCard/>
    </>
  );
};

export default App
