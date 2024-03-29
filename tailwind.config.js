/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.{js,vue,ts}",
    "./pages/**/*.{js,vue,ts}",
    "./plugins/**/*.{js,vue,ts}",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {
      colors: {
        "primary": "#D6073D",
        "primary-hover": "#C20C3C",
        "primary-active": "#AE113A",
        "accent": "#6FBC9A",
        "dashboard": "#EFF1F9",
        "exit": "#6F849C"
      },
    },
  },
  plugins: [],
}

