import socket
import termcolor

IP = "192.168.0.33"
PORT = 8081
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")

    if msg.startswith("GET / ") or msg.startswith("GET /index"):
        file = open('index.html', 'r')
        contents = file.read()
    elif msg.startswith("GET / blue") or msg.startswith("GET /blue.html"):
        file = open('blue.html', 'r')
        contents = file.read()
    elif msg.startswith("GET / pink") or msg.startswith("GET /pink.html"):
        file = open('pink.html', 'r')
        contents = file.read()
    else:
        file = open('error.html', 'r')
        contents = file.read()
    # Print the received message, for debugging
    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    # -- Everything is OK
    status_line = "HTTP/1.1 200 OK\r\n"

    # -- Build the header
    header = "Content-Type: text/html\r\n"
    header += "Content-Length: {}\r\n".format(len(str.encode(contents)))

    # -- Build the message by joining together all the parts
    response_msg = str.encode(status_line + header + "\r\n" + contents)
    cs.send(response_msg)

    # Close the socket
    cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
server_socket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
server_socket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(server_socket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = server_socket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(clientsocket)
