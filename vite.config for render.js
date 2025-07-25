import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  base: "./",  // ensures relative paths in dist/
  plugins: [react()],
  server: {
    port: 3000,
  },
});