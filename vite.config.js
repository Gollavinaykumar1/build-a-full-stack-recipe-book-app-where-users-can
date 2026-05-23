import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  base: "/build-a-full-stack-recipe-book-app-where-users-can/",
  build: { outDir: "dist", assetsDir: "assets" },
  server: { port: 3000 },
});
