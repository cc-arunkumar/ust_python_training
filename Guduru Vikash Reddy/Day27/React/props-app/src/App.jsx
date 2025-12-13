import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Card from './Card.jsx'
import './App.css'
import WeatherCard from './WeatherCard.jsx'
import ProductCard from './ProductCard.jsx'
import Greet from './Greet.jsx'
function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
    <Greet>
      <h2>Times of india</h2>
      <p>India won the match</p>

    </Greet>
     <Greet>
      <h2>sakshi</h2>
      <p>goodnews</p>
      
    </Greet>
    {/* <ProductCard name="Thumbsup" and price={40.00} rating={4}/>
    <ProductCard name="chapathi" and price={30.00}rating={5} />
    <ProductCard name="Biryani" and price={130.00}rating={5} />
    */}
      {/* <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p> */}
    </div>
  )
}

export default App
