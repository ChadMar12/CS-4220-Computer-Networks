# Lab 1 - Simple Web Server

A basic HTTP web server built with Python sockets that serves static files over HTTP/1.1.

## File Structure

```
.
├── README.md
├── lab1_server.py    # Main web server script
└── HelloWorld.html   # Example HTML file to serve (or any file you wish to request)
```

## Environment Info

- **Python:** 3.10+
- **OS:** Any (tested on Windows/macOS/Linux)
- **No external dependencies** — uses only Python standard library modules (`socket`, `sys`)

## Running Commands

1. **Start the server:**

   ```bash
   python lab1_server.py
   ```

   The server will start listening on `localhost` port `8080` and print `Ready to serve...`.

2. **Make a request:**

   Open a web browser and navigate to:

   ```
   http://localhost:8080/HelloWorld.html
   ```

   Replace `HelloWorld.html` with the name of any file located in the same directory as `lab1_server.py`.

3. **Stop the server:**

   Press `Ctrl + C` in the terminal to terminate the server.

## Notes

- The server handles one connection at a time (single-threaded).
- If the requested file is not found, the server returns a `404 Not Found` response.
- Requested files must be placed in the same directory as `lab1_server.py`.