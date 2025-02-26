import { ThemeProvider } from "@/components/theme-provider"
import { BrowserRouter as Router } from 'react-router-dom'
import AppSidebar from '@/components/Sidebar'
import Breadcrumbs from '@/components/Breadcrumbs'
import AppRouter from '@/components/AppRouter'
import { NavigationProvider } from '@/context/NavigationContext'

import {
  SidebarInset,
  SidebarProvider
} from "@/components/ui/sidebar"

// export default function App() {
//   return (
//     <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
//       <NavigationProvider>
//         <Router>
//           <SidebarProvider>
//             <AppSidebar />
//             <SidebarInset>
//               <Breadcrumbs />
//               <AppRouter />
//             </SidebarInset>
//           </SidebarProvider>
//         </Router>
//       </NavigationProvider>
//     </ThemeProvider>
//   )
// }

import React, { useEffect, useState } from "react";

export default function App() {
  const [backendMessage, setBackendMessage] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/message")
      .then((response) => response.json())
      .then((data) => setBackendMessage(data.message))
      .catch((error) =>
        console.error("Error fetching backend message:", error)
      );
  }, []);

  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <NavigationProvider>
        <Router>
          <SidebarProvider>
            <AppSidebar />
            <SidebarInset>
              <Breadcrumbs />
              {/* Display the backend message */}
              <div style={{ textAlign: "center", margin: "20px 0" }}>
                <h2>Backend Message</h2>
                <p>{backendMessage || "Loading backend message..."}</p>
              </div>
              <AppRouter />
            </SidebarInset>
          </SidebarProvider>
        </Router>
      </NavigationProvider>
    </ThemeProvider>
  );
}

// import React, { useEffect, useState } from "react";
//
// function App() {
//   const [message, setMessage] = useState("");
//
//   useEffect(() => {
//     // Fetch data from Flask backend
//     fetch("http://127.0.0.1:5000/api/message")
//       .then((response) => response.json())
//       .then((data) => setMessage(data.message))
//       .catch((error) => console.error("Error fetching message:", error));
//   }, []);
//
//   return (
//     <div style={{ textAlign: "center", marginTop: "50px" }}>
//       <h1>My Flask + React Example</h1>
//       <p>{message || "Loading Backend message..."}</p>
//     </div>
//   );
// }
//
// export default App;




