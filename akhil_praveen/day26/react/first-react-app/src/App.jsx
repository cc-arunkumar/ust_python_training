import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Greet from './Greet'

export default function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <h1>Welcome</h1>
    <Greet distance = "Apple"/>
    <Greet distance = "Banana"/>
    <Greet distance = "Egg"/>
    <Greet distance = "Carrot"/>
    <Greet distance = "Mango"/>
    <Greet distance = "Rose"/>
    </>
  )
}