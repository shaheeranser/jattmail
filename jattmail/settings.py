# Connection settings
ADDRESS = "127.0.0.1"   # IP Address (user 0.0.0.0 for available IP)
PORT = 2500               # Port number (Defualt 25 for SMTP)
CONNECTIONS = 5         # Number of devices connected at a time
TIMEOUT = 0.1           # Seconds

# Log settings
LOG_ECHO = True         # Print logs on console
LOG_WRITE = True        # Write logs in a log file
LOG_FILE = "logs.txt"   # Log file name

# Control settings
BREAK = "exit()"        # Stops the server if break message received
