import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import GreetingCard from './GreetingCard'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <GreetingCard name="7.7 MAGNITUDE" views="2.3M"
      musicUrl="https://open.spotify.com/embed/track/1xofPJhZcfJCc66P1UAh28?utm_source=generator"/>
      <GreetingCard name="P-POP CULTURE" views="1.4M"
      musicUrl="https://open.spotify.com/embed/track/1xofPJhZcfJCc66P1UAh28?utm_source=generator"/>
      <GreetingCard name="MF GABRU" views="1.0M"
       musicUrl="https://open.spotify.com/embed/track/1xofPJhZcfJCc66P1UAh28?utm_source=generator"/>
    </>
  )
}

export default App
