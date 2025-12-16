/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {extend: {
  keyframes: {
    gradient: {
      "0%": { backgroundPosition: "0% 50%" },
      "50%": { backgroundPosition: "100% 50%" },
      "100%": { backgroundPosition: "0% 50%" },
    },
    fadeIn: {
      "0%": { opacity: 0, transform: "translateY(20px)" },
      "100%": { opacity: 1, transform: "translateY(0)" },
    },
    pulseSlow: {
      "0%": { opacity: 0.4, transform: "scale(1)" },
      "50%": { opacity: 0.7, transform: "scale(1.1)" },
      "100%": { opacity: 0.4, transform: "scale(1)" },
    },
    pulseSlower: {
      "0%": { opacity: 0.3, transform: "scale(1)" },
      "50%": { opacity: 0.6, transform: "scale(1.15)" },
      "100%": { opacity: 0.3, transform: "scale(1)" },
    },
  },
  animation: {
    gradient: "gradient 8s ease infinite",
    fadeIn: "fadeIn 0.8s ease-out",
    "pulse-slow": "pulseSlow 6s ease-in-out infinite",
    "pulse-slower": "pulseSlower 10s ease-in-out infinite",
  },
}
},
  },
  plugins: [],
};
