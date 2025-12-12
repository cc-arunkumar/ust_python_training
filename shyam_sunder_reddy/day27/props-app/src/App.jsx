import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import GreetingCard from './GreetingCard'
import WeatherCard from './WeatherCard.jsx'
import ProductCard from './ProductCard.jsx'
import Card from './Card.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      {/* <h1>UST PORTAL</h1>
      <GreetingCard colorname="left" name="SHYAM" message="Namaste"/>
      <GreetingCard colorname="right" name="RAM" message="Vanakam"/>
      <GreetingCard colorname="left" name="ANJAN" message="Greetings"/>
      <GreetingCard colorname="right" name="ARUN" message="Hola"/>
      
      <WeatherCard city="Hyderabad" temperature={19}/>
      <WeatherCard city="Kerala" temperature={27}/>
      <WeatherCard city="Benguluru" temperature={17}/>
      <WeatherCard city="Pune" temperature={25}/>

      <ProductCard name="munch" price={20.00} rating={4.5}/>
      <ProductCard name="Lays" price={10.50} rating={3.5}/>
      <ProductCard name="Oreo" price={5.25} rating={4.9}/>
      <ProductCard name="Coffee" price={35.25} rating={4.0}/> */}

      <Card>
        <h2>Times of India News</h2>
        <hr/>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut, reprehenderit.</p>
      </Card>

      <Card>
        <h2>Sakshi</h2>
        <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Blanditiis dicta deserunt necessitatibus tempore eos odit accusantium consequuntur aliquam cupiditate iste, rem quia a molestiae cum autem, illo omnis itaque amet.</p>
      </Card>

    </>
  )
}

export default App
