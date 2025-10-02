/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'cyber-dark': '#0a1628',
        'cyber-blue': '#00f0ff',
        'cyber-purple': '#8b5cf6',
      }
    },
  },
  plugins: [],
}
