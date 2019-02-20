import socket

PORT = 8087
IP = "212.128.253.70"
MAX_OPEN_REQUESTS = 5


def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""
    if msg == "EXIT":
        cs.close()
    else:
        # Read client message. Decode it as a string
        msg = cs.recv(2048).decode("utf-8")

        # Print the received message, for debugging
        termcolor.cprint(msg, "red")

        # Send the msg back to the client (echo)
        cs.send(str.encode(msg))

        # Close the socket
        cs.close()


# MAIN PROGRAM

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP and PORT
serversocket.bind((IP, PORT))

# Configure the server sockets
# MAX_OPEN_REQUESTS connect requests before refusing outside connections
serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:
    # accept connections from outside
    # The server is waiting for connections
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # Service the client
    process_client(cli