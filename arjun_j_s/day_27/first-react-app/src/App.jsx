import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Greet from './Greet'
import Hello from './Hello'
import Weather from './Weather'
import Product from './Product'
import Card from './Card'

export default function App() {

  return (
    <>
    <h1>Heheheheh :)</h1>
      {/* <Greet first={["GoldenMango","sunny yellow juicy fruit"]} second={["Pineapple","tropical fruit delicious"]}/>
      <Greet first={["BrightOrange","citrus burst refreshment"]} second={["Strawberry","refreshingly sweet taste"]}/> */}
      {/* <Hello first={["RAM","Namaste"]} second={["Shyam","Vanakkam"]}/>
      <Hello first={["RAVI","Namaskaaram"]} second={["BIJU","Hehehe"]}/> */}
      {/* <Weather city={["New Delhi","Mumbai"]} temp={[22,23]}/>
      <Weather city={["Kolkata","Chennai"]} temp={[24,25]}/> */}
      {/* <Product name={["Munch","Diary Milk","KitKat"]}
      cost={[10,40,20]} rating={[5.9,8.8,7.3]} */}
       {/* /> */}
       <Card>
        <h2>Times of India News</h2>
        <p>ISRO successfully launches new SSLV rocket today!!</p>
       </Card>
    </>
  )
}

