import { defineConfig } from "vite";
import djangoVite from "django-vite-plugin";

export default defineConfig({
server: {
        cors: {
            origin: 'http://127.0.0.1:8000',
        },
    },
    plugins: [
        djangoVite({
            input: [
                "./static/js/adda-entry.js",
                "./static/js/main.js",
                "./static/css/tailwind.css"
            ],
            pyPath: "python3"
        }),
    ],
});