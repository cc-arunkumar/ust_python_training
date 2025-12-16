import React from "react";
import { Button } from "../components/ui/button"; // adjust path as needed
import { ArrowRight } from "lucide-react"; // icon import

const CiaSection = () => {
  return (
    <section className="w-full ">
      <div className="mx-auto py-24 gradient rounded-lg">
        <div className="flex flex-col items-center justify-center space-y-4 text-center max-w-3xl mx-auto">
          <h2 className="text-3xl font-bold tracking-tighter text-white sm:text-4xl md:text-5xl">
            Ready to Simplify Project Management?
          </h2>
          <p className="mx-auto max-w-150 text-white md:text-xl">
            Experience Jira Lite — a lightweight, powerful platform to manage tasks,
            track progress, and collaborate seamlessly with your team.
          </p>
          <a href="/dashboard">
            <Button
              size="lg"
              variant="secondary"
              className="h-11 mt-5 animate-bounce"
            >
              Get Started with Jira Lite{" "}
              <ArrowRight className="ml-2 h-4 w-4" />
            </Button>
          </a>
        </div>
      </div>
    </section>
  );
};

export default CiaSection;
