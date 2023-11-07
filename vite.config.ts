import { defineConfig } from 'vite'
import solid from 'vite-plugin-solid'

export default defineConfig({
  root: 'frontend',
  build: {
    outDir: 'static',
  },
  plugins: [solid()],
});
