import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import WeatherCard from './WeatherCard'
import ProductCard from './ProductCard'
import Card from './Card'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <h1>News of the Day!</h1>
     {/* <WeatherCard city = "Hyderabad"  degree = {22}/>
     <WeatherCard city = "Bangalore" degree = {24}/>
     <WeatherCard city = "Chennai"  degree = {27}/>
     <WeatherCard city = "Trivandrum"  degree = {26}/> */}

     {/* <ProductCard name = "Munch"  price = {15} rating = {4.9}/>
     <ProductCard  name = "Five Star"  price = {20} rating = {4.5}/>
     <ProductCard  name = "Gems"   price = {10} rating = {4.0}/>
     <ProductCard  name = "Dairy Milk"  price = {12} rating = {4.7}/> */}

     <Card>
      <h2>Times of India News</h2>
      <hr />
      <p> ISRO successfully launches new SSLV Rocket</p>
     </Card>

     <Card>
      <h2>Sports News</h2>
      <hr />
      <p> INDIA Won ICC World Cup</p>
     </Card>


     
    </>
  )
}

export default App
