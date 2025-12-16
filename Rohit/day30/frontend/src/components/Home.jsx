import React, { useEffect, useRef } from "react";
import { Button } from "../components/ui/button"; // adjust path as needed
// import banner2 from "../assets/banner2.jpeg"
import front_image from "../assets/front_image.png";
const Home = () => {
  const imageRef = useRef(null);

  useEffect(() => {
    const imageElement = imageRef.current;

    const handleScroll = () => {
      const scrollPosition = window.scrollY;
      const scrollThreshold = 100;

      if (scrollPosition > scrollThreshold) {
        imageElement.classList.add("scrolled");
      } else {
        imageElement.classList.remove("scrolled");
      }
    };

    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <section className="w-full pt-5 md:pt-10 pb-10">
        <div className="grid-background"></div>
      <div className="space-y-6 text-center">
        <div className="space-y-6 mx-auto">
          <h1 className="text-3xl font-bold md:text-6xl lg:text-7xl xl:text-8xl gradient-title animate-gradient">
            Jira Lite
            <br />
            Simplify Your Project Management
          </h1>
          <p className="mx-auto max-w-150 text-muted-foreground md:text-xl">
            Manage tasks, track progress, and collaborate with your team — all in a
            lightweight, easy‑to‑use Jira alternative built for speed and simplicity.
          </p>
        </div>

        {/* Buttons */}
        <div className="flex justify-center space-x-4">
          <a href="/dashboard">
            <Button size="lg" className="px-8">
              Get Started
            </Button>
          </a>
          <a href="#">
            <Button size="lg" variant="outline" className="px-8">
              Watch Demo
            </Button>
          </a>
        </div>

        {/* Image */}
        <div className="hero-image-wrapper mt-5 md:mt-0">
          <div ref={imageRef} className="hero-image">
            <img
              src={front_image}
              width={1000}
              height={520}
              alt="Jira Lite Dashboard Preview"
              className="rounded-lg shadow-2xl border mx-auto"
            />
          </div>
        </div>
      </div>
    </section>
  );
};

export default Home;
