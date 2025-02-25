# How to Run Your React (Vite) Project


### 1 Install Dependencies
- Ensure you’re in the root folder of the project (the same folder that contains `package.json`).  
- Run:

```bash
npm install
```

### 2 Start the Development Server

Once dependencies are installed, start your project using:

```bash
npm run dev
```

This will start the Vite development server, and you should see output similar to:

```bash
VITE vX.X.X  ready in XX ms
➜  Local: http://localhost:5173/
➜  Network: use --host to expose
```

Open the provided URL (http://localhost:5173/) in your browser to view the application.

### 3. Running a Production Build

When you’re ready to deploy your app, follow these steps to build and preview a production-ready version:

- Build the App: Run the following command in your terminal:

```bash
npm run build
```

This command creates an optimized production build in a folder typically named dist.

- Preview the Production Build: To locally preview the production build, run:

```bash
npm run preview
```

Vite will start a server that serves the contents of the dist folder, simulating a production environment.

3.3 Deploying the Production Build
	•	The content s of the dist folder are static assets (HTML, CSS, JS) that can be deployed to any static file server or hosting platform such as Netlify, Vercel, or GitHub Pages.

### About Vite

Vite is a fast build tool and development server optimized for modern web projects, particularly for frameworks like React. Here’s what you need to know:   
	•	Lightning Fast Startup: Vite leverages native ES modules, eliminating the need for bundling during development. This results in near-instant startup times.   
	•	Hot Module Replacement (HMR): Code changes are applied instantly without needing a full page reload, making the development process more efficient.   
	•	Optimized Build Process: When you build your project for production, Vite uses Rollup under the hood to bundle and optimize your code, resulting in fast and efficient production builds.   
	•	Easy Configuration: You can customize Vite’s behavior through a configuration file (vite.config.ts or vite.config.js), which allows you to adjust settings such as plugins, server options, and build options.   

