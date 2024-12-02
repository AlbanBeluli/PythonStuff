import http.server
import socketserver

def get_port():
    """Asks the user if they want to use the standard port or specify a custom one."""
    choice = input("Do you want to use the standard port (8000)? (y/n): ").lower()
    if choice == 'y':
        return 8000
    else:
        while True:
            try:
                port = int(input("Please enter the port number you want to use: "))
                if 1 <= port <= 65535:  # Valid port range
                    return port
                else:
                    print("Port must be between 1 and 65535. Try again.")
            except ValueError:
                print("Please enter a valid number for the port.")

# Get the port from user input or default to 8000
PORT = get_port()

# Define the server handler
Handler = http.server.SimpleHTTPRequestHandler

# Create the server with the specified port
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    try:
        # Start the server
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Handle keyboard interrupt for graceful shutdown
        print("\nServer stopped by user")
