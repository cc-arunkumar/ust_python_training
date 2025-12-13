import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
// import GreetingCard from "./GreetingCard";
// import WeatherCard from "./WeatherCard";
// import ProductCard from "./ProductCard";
// import Card from "./Card";
import EmployeeCard from "./EmployeeCard";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="app-container">
      <h1 className="heading">HELLO....👋😊</h1>

      <div className="cards-container">
        <div className="left-group">
          {/* <GreetingCard
            bgColor="linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
            name="RAM"
            text="Namaste"
          />
          <GreetingCard
            bgColor="linear-gradient(to right, #00d2ff 0%, #3a47d5 100%)"
            name="Felix"
            text="React is Amazing"
          /> */}
          {/* <GreetingCard bgColor="lightblue" text="React practices...." />  */}
          {/* <WeatherCard
            bgColor="linear-gradient(to right, #00d2ff 0%, #3a47d5 100%)"
            city="Bangalore"
            temperature={25}
          />
          <WeatherCard
            bgColor="linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
            city="Delhi"
            temperature={30}
          /> */}
          {/* <ProductCard
            bgColor="linear-gradient(to top, #fbc2eb 0%, #a6c1ee 100%)"
            product="ThumpsUp"
            price={12.9}
            rating={3.5}
          />
          <ProductCard
            bgColor="linear-gradient(to top, #fbc2eb 0%, #a6c1ee 100%)"
            product="Maaza"
            price={19.9}
            rating={4.5}
          /> */}
          {/* <Card bgColor="linear-gradient(to top, #fbc2eb 0%, #a6c1ee 100%)">
            <h2>Deccan Chronicle</h2>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente
              minus officia deserunt, saepe possimus doloremque sed tenetur
              voluptatem accusantium hic cupiditate eveniet ab soluta reiciendis
              repellat officiis, itaque, magnam necessitatibus!
            </p>
          </Card> */}
          <EmployeeCard
            bgColor="linear-gradient(to top, #fbc2eb 0%, #a6c1ee 100%)"
            img_url="./pexels-fotios-photos-10033194.jpg"
            name="Arun Reddy"
            employee_id={1234}
            role={"Developer"}
            location="Bangalore"
          />
        </div>
        <div className="right-group">
          <EmployeeCard
            bgColor="linear-gradient(to left, #fbc2eb 0%, #a6c1ee 100%)"
            name="Felix Sabu"
            img_url="./pexels-tphotography-92129.jpg"
            employee_id={1024}
            role={"Developer-I"}
            location="Chennai"
          />
          {/* <GreetingCard
            bgColor="linear-gradient(to top, #fbc2eb 0%, #a6c1ee 100%)"
            name="Shyam"
            text="Vanakam"
          />
          <GreetingCard
            bgColor="linear-gradient(135deg, #fa709a 0%, #fee140 100%)"
            name="ARUN"
            text="hello, Arun Welcome !"
          /> */}
          {/* <GreetingCard
            bgColor="#fda4af"
            text="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsam, quod ipsum blanditiis reprehenderit, a maxime asperiores veritatis debitis omnis veniam obcaecati illo, architecto vero perspiciatis recusandae? Molestias ut eos quas!"
          />  */}
          {/* <WeatherCard
            bgColor="linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
            city="Hyderabad"
            temperature={35}
          />
          <WeatherCard
            bgColor="linear-gradient(to top, #fbc2eb 0%, #a6c1ee 100%)"
            city="Chennai"
            temperature={43}
          /> */}
          {/* <ProductCard
            bgColor="linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
            product="7Up"
            price={12.9}
            rating={3.5}
          /> */}
          {/* <Card bgColor="linear-gradient(to top, #fbc2eb 0%, #a6c1ee 100%)">
            <h2>Times of India </h2>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente
              minus officia deserunt, saepe possimus doloremque sed tenetur
              voluptatem accusantium hic cupiditate eveniet ab soluta reiciendis
              repellat officiis, itaque, magnam necessitatibus!
            </p>
          </Card> */}
        </div>
      </div>
    </div>
  );
}

export default App;
