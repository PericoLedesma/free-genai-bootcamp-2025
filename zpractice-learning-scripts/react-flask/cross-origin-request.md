## What are Cross-Origin Requests?

**Cross-origin requests** occur when a web page makes an HTTP request to a domain different from the one that served the web page. An "origin" is defined by the combination of the protocol (http/https), domain, and port.

### Why It Matters

Browsers enforce a security measure known as the **Same-Origin Policy**, which restricts how scripts loaded from one origin can interact with resources from another origin. This is a key security feature to prevent malicious websites from reading sensitive data from another domain.

### How Cross-Origin Requests Work

- When a web page from one origin (e.g., `https://example.com`) tries to fetch data from another origin (e.g., `https://api.anotherdomain.com`), the browser checks if the server at the second origin allows such requests.
- The server must include specific **CORS (Cross-Origin Resource Sharing)** headers (like `Access-Control-Allow-Origin`) in its response to grant permission for the cross-origin request.
- If the correct CORS headers are present, the browser allows the web page to access the data. Otherwise, the request is blocked for security reasons.

### In Summary

- **Cross-Origin Requests:** HTTP requests made from one origin to a different origin.
- **Same-Origin Policy:** A browser security feature that restricts these requests by default.
- **CORS:** A protocol that allows servers to specify who can access their resources via cross-origin requests.

This mechanism is essential for enabling web applications (like a React frontend) to securely fetch data from a backend server (like one built with Flask) that might be hosted on a different domain.