import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Greet from './Greet'

export default function App() {

  return (
    <>
    <h1>Heheheheh :)</h1>
      <Greet first={["GoldenMango","sunnyyellowjuicyfruit"]} second={["Pineapple","tropicalfruitdelicious"]}/>
      <Greet first={["BrightOrange","citrusburstrefreshment"]} second={["Strawberry","refreshinglysweettaste"]}/>
    </>
  )
}

