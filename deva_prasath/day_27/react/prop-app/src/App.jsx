import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import {Greet,Greet1} from './Greet'
import GreetingCard from './GreetingCard'
import WeatherCard from './WeatherCard'
import ProductCard from './ProductCard'
import Card from './Card'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    {/* <h1>Helooo Carol</h1>
    <Greet />
    <Greet1 />
    <Greet />
    <Greet1 /> */}
    <h1>Good Morning</h1>
    {/* <GreetingCard name="Ram" greet="Namste"/>
    <GreetingCard name="Shyam" greet="Vanakkam"/>
    <GreetingCard name="Dustin" greet="Hello"/>
    <GreetingCard name="Hitler" greet="Guten tag"/>
 */}
    {/* <WeatherCard city="New Delhi" temperature= "22 C"/>
    <WeatherCard city="Mumbai" temperature= "23 C"/>
    <WeatherCard city="Kolkata" temperature= "24 C"/>
    <WeatherCard city="Chennai" temperature= "25 C"/> */}
     {/* <ProductCard name="Cetaphil" price={200} rating={4.9}/>
     <ProductCard name="Minimalist" price={300} rating={4.4}/>
     <ProductCard name="Derma-G" price={400} rating={4.3}/> */}
    <Card>
      <h2>Times of India news</h2>
      <hr />
      <p>ISRO successfully launches new SSLV rocket today!</p>
    </Card>
    <Card>
      <h2>Sports News</h2>
      <p>India won the T20 World Cup</p>
    </Card>

    
    </>
  )
}

export default App
