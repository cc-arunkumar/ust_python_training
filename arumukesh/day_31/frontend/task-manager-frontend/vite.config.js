import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/login": {
        // Proxy the login route
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
        secure: false,
      },
      "/api": {
        // Proxy all your /api/v1 routes
        target: "http://127.0.0.1:8000",
        changeOrigin: true,
        secure: false,
      },
      configure: (proxy) => {
        proxy.on("proxyReq", (proxyReq, req) => {
          console.log("Proxying request:", req.method, req.url);
        });
      },
    },
  },
});
