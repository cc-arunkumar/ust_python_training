import React, { useRef } from "react";
import Autoplay from "embla-carousel-autoplay";

import { Card, CardContent } from "../components/ui/card"; // adjust path
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "../components/ui/carousel"; // adjust path

export function CarouselPlugin() {
  const plugin = useRef(
    Autoplay({ delay: 2000, stopOnInteraction: true })
  );

  const images = [
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470?q=80&w=800",
    "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=800",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=800",
    "https://images.unsplash.com/photo-1529333166437-7750a6dd5a70?q=80&w=800",
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c?q=80&w=800",
  ];

  return (
    <Carousel
      plugins={[plugin.current]}
      className="w-full max-w-md"
      onMouseEnter={plugin.current.stop}
      onMouseLeave={plugin.current.reset}
    >
      <CarouselContent>
        {images.map((src, index) => (
          <CarouselItem key={index}>
            <div className="p-1">
              <Card>
                <CardContent className="flex aspect-square items-center justify-center p-0">
                  <img
                    src={src}
                    alt={`Unsplash demo ${index + 1}`}
                    className="w-full h-full object-cover rounded-lg"
                  />
                </CardContent>
              </Card>
            </div>
          </CarouselItem>
        ))}
      </CarouselContent>
      <CarouselPrevious />
      <CarouselNext />
    </Carousel>
  );
}
