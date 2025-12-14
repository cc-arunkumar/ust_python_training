import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import GreetingCard from './GreetingCard'
import ProductCard from './ProductCard'
import Card from './Card'
import WeatherCard from './WeatherCard'

function App() {

  return (
    <>
      
      <GreetingCard name="Ram"greet="Namaste"/>
      <GreetingCard name="Shyam"greet="Vanakkam"/>
      <GreetingCard name="Ashutosh"greet="Hello"/>
      <GreetingCard name="Deva"greet="greetings"/>
    
      <div><h2>Weather Card</h2></div>
      <div>
      <WeatherCard city = "Mumbai"temp="30"/>
      <WeatherCard city = "Delhi"temp="35"/>
      <WeatherCard city = "Bangalore"temp="24"/>
      </div>

      <div><h2>Product Card</h2></div>
      <div>
      <ProductCard name="Amul"price="50"ratings="4.6"/>
      <ProductCard name="MilkMist"price="45"ratings="4.0"/>
      <ProductCard name="Ordinary"price="100"ratings="4.6"/>
      </div> 

        <Card>
          <h2>Times of India News</h2>
          <hr/>
          <p>ISRO successfully launches new SSLV rocket today!</p>
        </Card>
        <Card>
          <h2>Sports News</h2>
          <hr/>
          <p>INDIA Wins the T20 World Cup</p>
        </Card>
      
    </>
  )
}

export default App
