import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Product from './ProductCard'
import Card from './Card'

export default function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <h1>Welcome</h1>
    <div className='card_container'>
      {/* <Product city = "New Delhi" temp = "22" cardname = "card1"/>
      <Product city = "Mumbai" temp = "23" cardname = "card2"/>
      <Product city = "Kolkata" temp = "24" cardname = "card1"/>
      <Product city = "Chennai" temp = "25" cardname = "card2"/> */}
      
      {/* <Product name = "Munch" price = {10} rating = {9} cardname = "card1"/>
      <Product name = "5 star" price = {15} rating = {10} cardname = "card2"/>
      <Product name = "Perk" price = {20} rating = {8} cardname = "card1"/>
      <Product name = "Bounty" price = {5} rating = {5} cardname = "card2"/> */}

      <Card cardname='card1'>
        <div>
        <h2>Times of India News</h2>
        <hr />
        <p>ISRO successfully launches new SSLV rocket today!</p>
        </div>
      </Card>
      
      <Card cardname='card2'>
        <div>
        <h2>Sports News</h2>
        <hr />
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam, veritatis?</p>
        </div>
      </Card>

    </div>
    
    </>
  )
}