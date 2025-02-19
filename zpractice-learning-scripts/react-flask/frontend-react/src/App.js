import React, { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    // Fetch data from Flask backend
    fetch("http://127.0.0.1:5000/api/message")
      .then((response) => response.json())
      .then((data) => setMessage(data.message))
      .catch((error) => console.error("Error fetching message:", error));
  }, []);

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>My Flask + React Example</h1>
      <p>{message || "Loading Backend message..."}</p>
    </div>
  );
}

export default App;