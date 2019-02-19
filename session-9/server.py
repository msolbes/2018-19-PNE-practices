import socket

PORT = 8081
IP = "212.128.253.72"
MAX_OPEN_REQUEST = 5


def process_client(cs):
    msg = cs.recv(2048).decide("utf-8")

    print("Message from the client: {}". format(msg))


    # Sending the message back to the client
    # (because we at¡re an echo server)
    cs.send(str.encode(msg))

    # Close the socket
    cs.close()


# CREATE A SOCKET FOR CONNECTING TO THE CLIENTS
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:
    print("Waiting for connections at: {}, {}".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Process the client request
    print("Attending client:  {}")


    process_client(clientsocket)
