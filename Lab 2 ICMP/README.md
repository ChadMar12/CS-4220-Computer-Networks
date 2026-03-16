# Lab 2 - ICMP Pinger

A custom Ping application built with Python raw sockets that sends ICMP Echo Request packets and listens for Echo Reply responses to measure round-trip time, TTL, and packet loss.

## File Structure

```
.
├── README.md
└── Lab2_icmp_pinger.py    # ICMP Ping client script
```

## Environment Info

- **Python:** 3.10+
- **OS:** Any (tested on Windows/macOS/Linux)
- **Privileges:** Requires administrator/root privileges for raw socket access
- **No external dependencies** — uses only Python standard library modules (`socket`, `os`, `sys`, `struct`, `time`, `select`)

## Running Commands

1. **Run the pinger (Linux/macOS):**

   ```bash
   sudo python Lab2_icmp_pinger.py
   ```

   On **Windows**, run the terminal as Administrator:

   ```bash
   python Lab2_icmp_pinger.py
   ```

2. **Change the target host:**

   Edit the `ping()` call at the bottom of the script:

   ```python
   ping("127.0.0.1")        # localhost
   ping("google.com")       # or any remote host
   ```

3. **Stop the pinger:**

   Press `Ctrl + C` in the terminal to terminate the program.

## Notes

- The pinger sends one ICMP Echo Request per second and waits up to one second for each reply.
- Each response displays the source IP, sequence number, TTL, and round-trip time in milliseconds.
- If no reply is received within the timeout window, `Request timed out.` is printed.
- Raw sockets require elevated privileges on most operating systems.
