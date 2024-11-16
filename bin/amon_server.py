import socket
import psutil
import time

# Function to get logged-in users
def get_logged_users():
    users = []
    for user in psutil.users():
        users.append(f"{user.name} ({user.host})")
    return users

# Function to get a unique custom message for each server
def get_custom_message():
    return "Welcome to the Linux system!"

# Server code
def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server started on {host}:{port}. Waiting for connection...")

    while True:
        # Accept incoming connections
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")

        try:
            # Fetch the list of logged users and the custom message
            logged_users = get_logged_users()
            custom_message = get_custom_message()

            # Prepare the response string
            response = ""
            for user in logged_users:
                response += f"{user:<30} | {custom_message}\n"  # <30 aligns the username column to the left

            # Send the response
            client_socket.sendall(response.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()
            time.sleep(1)

# Start the server
if __name__ == "__main__":
    host = "0.0.0.0"  # Listen on all available interfaces
    port = 12345  # Port to listen on

    start_server(host, port)
