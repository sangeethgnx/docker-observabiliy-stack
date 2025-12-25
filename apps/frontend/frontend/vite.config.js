import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

setInterval(() => {
  console.log('[FRONTEND SERVER LOG]', Math.floor(Math.random() * 1000))
}, 1000)

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
})
