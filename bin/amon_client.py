import socket
import curses
import time

_SOCKET_TIMEOUT  = 3000
_SOCKET_MAXLEN   = 4096
_CURSE_REFRESH_S = 1

# Function to connect to a server and fetch data
def fetch_data_from_server(server_ip, server_port):
    try:
        # Establish connection with the server
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.settimeout(2)
        with mysock as s:
            s.connect((server_ip, server_port))
            # Receive data (max 4096 bytes)
            data = s.recv(_SOCKET_MAXLEN).decode('utf-8')
            return data
    except Exception as e:
        #return f"Error connecting to server {server_ip}: {str(e)}"
        return

# Function to display data in a TUI
def display_data(stdscr, all_server_data):
    # Clear the screen
    stdscr.clear()

    # Colors setup
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # For logged users
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # For custom message
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)  # For custom message

    # Initialize the y position for displaying each server's data
    y = 1

    if(not(all_server_data)):
        return

    # Display data for each server
    for server_ip, server_data in all_server_data.items():
        # Split the server data into lines
        lines = server_data.split("\n")

        # Extract the custom message (first line of the response)
        custom_message = lines[0].split(" | ")[1] if lines else "No message received"

        # Title for each server
        if "FREE" in custom_message:
            #stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y, 0, f"Server {server_ip} : {custom_message}", curses.color_pair(2) | curses.A_BOLD )
            #stdscr.attroff(curses.color_pair(2))
        else:
            #stdscr.attron(curses.color_pair(3))
            stdscr.addstr(y, 0, f"Server {server_ip} : {custom_message}",curses.color_pair(3) | curses.A_BOLD)
            #stdscr.attroff(curses.color_pair(3))

        y += 1  # Skip a line after the header

        # Extract the logged users (all subsequent lines)
        logged_users = []
        for line in lines:
            if line.strip():  # Ignore empty lines
                user, message = line.split(" | ")
                user = user.rstrip()
                if("root" not in user):
                   logged_users.append(user)

        # Display logged users as a comma-separated list
        users_line = ", ".join(logged_users)
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(y, 2, users_line)
        stdscr.attroff(curses.color_pair(1))

        y += 2  # Leave space between server blocks

    # Refresh the screen
    stdscr.refresh()

# Main function to run the client with polling
def main(stdscr):
    # Define a list of server IP addresses and ports
    server_ips = ["192.168.8.140","192.168.8.153","192.168.8.151","192.168.8.132",]  # List of server IPs
    server_port = 12345  # Port used by the server

    # Polling interval (in seconds)
    polling_interval = _CURSE_REFRESH_S

    # Dictionary to store data from each server
    all_server_data = {}

    # Allow user to quit by pressing 'q'
    stdscr.nodelay(1)  # Non-blocking input


    while True:
        # Fetch data from each server
        for server_ip in server_ips:
            try:
               server_data = fetch_data_from_server(server_ip, server_port)
               if(server_data):
                  all_server_data[server_ip] = server_data
            except:
                pass

        # Display the collected data in the TUI
        display_data(stdscr, all_server_data)

        # Wait for the polling interval before the next refresh
        time.sleep(polling_interval)

        # Check if the user pressed 'q' to exit
        if stdscr.getch() == ord('q'):
            break

# Start the client
if __name__ == "__main__":
    print("="*40)
    print("ASTRIAL MONITOR v.1.0")
    print("="*40)

    curses.wrapper(main)
