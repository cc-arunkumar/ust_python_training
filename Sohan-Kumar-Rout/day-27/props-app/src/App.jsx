import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import GreetingCard from './GreetingCard'
import Weather from './Weather'
import ProductCard from './ProductCard'
import Card from './Card'
import EmployeeCard from './EmployeeCard'
import EmployeeList from './EmployeeList'
import ProjectTeam from './ProjectTeam'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <h1>Cards</h1>
      <GreetingCard  name = "Sohan" greet="Namaste!"/>
      <GreetingCard name = "Rahul" greet="Vanakkam!"/>
      <GreetingCard name = "Sovan" greet="Namaskar!"/>
      <GreetingCard name = "Naveen" greet="Apan Mane Khusi ta !!"/>
    <h2>Cities</h2>
      <Weather city="Bhubaneswar" temperature={22} />
      <Weather city="Bangalore" temperature={24} />
      <Weather city="Gurgaon" temperature={13} />
      <Weather city="Mumbai" temperature={12} />
    <h2>Product List</h2>
    <div className="product-list">
      <ProductCard name="sha" price={300} rating={5.32} />
      <ProductCard name="Laptop" price={50000} rating={4.8} />
      <ProductCard name="Mobile" price={15000} rating={4.2} />
      <ProductCard name="Watch" price={2000} rating={4.5} />
    <h2>News</h2>
    <Card>
      <h2>Times of India</h2>
      <hr/>
      <p>ISRO successfully launches new SSLV rocket today !</p>
    </Card>
    <Card>
      <h2>Sports News</h2>
      <hr />
      <p>India won the T20 match in Barabati Stadium Cuttack !</p>
    </Card>
    <EmployeeList />
    <ProjectTeam/>
    </div>






    </>
  )
}

export default App
