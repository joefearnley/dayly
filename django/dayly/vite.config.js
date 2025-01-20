import { defineConfig } from "vite";
import djangoVite from "django-vite-plugin";

export default defineConfig({
    plugins: [
        djangoVite({
            input: ["./static/js/main.js", "./static/css/tailwind.css"],
            pyPath: "python3"
        }),
    ],
});