import { ThemeProvider } from "@/components/theme-provider"
import { BrowserRouter as Router } from 'react-router-dom'
import AppSidebar from '@/components/Sidebar'
import Breadcrumbs from '@/components/Breadcrumbs'
import AppRouter from '@/components/AppRouter'
import { NavigationProvider } from '@/context/NavigationContext'
import React, { useEffect, useState } from "react";

import {
  SidebarInset,
  SidebarProvider
} from "@/components/ui/sidebar"

// import {StudyStats} from "@/services/api.ts";

export default function App() {
  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <NavigationProvider>
        <Router>
          <SidebarProvider>
            <AppSidebar />
            <SidebarInset>
              <Breadcrumbs />
              <AppRouter />
            </SidebarInset>
          </SidebarProvider>
        </Router>
      </NavigationProvider>
    </ThemeProvider>
  )
}





/// First try to connect to backend. Lets go back to the original code
// export default function App() {
//   const [backendMessage, setBackendMessage] = useState("");
//
//   useEffect(() => {
//     fetch("http://127.0.0.1:8000/api/message")
//       .then((response) => response.json())
//       .then((data) => setBackendMessage(data.message))
//       .catch((error) =>
//         console.error("Error fetching backend message:", error)
//       );
//   }, []);
//
//
//   return (
//     <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
//       <NavigationProvider>
//         <Router>
//           <SidebarProvider>
//             <AppSidebar />
//             <SidebarInset>
//               <Breadcrumbs />
//               {/* Display the backend message */}
//               <div style={{ textAlign: "center", margin: "20px 0" }}>
//                 <h2>Backend Message</h2>
//                 <p>{backendMessage || "Loading backend message..."}</p>
//               </div>
//               <AppRouter />
//             </SidebarInset>
//           </SidebarProvider>
//         </Router>
//       </NavigationProvider>
//     </ThemeProvider>
//   );
// }





