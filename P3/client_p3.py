import socket

PORT = 1112
IP = "158.42.240.34"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

condition = True
while condition:

    msg = ("AACCGTGA"
           "len"
           "complement")

    s.send(str.encode(msg))

    # Receive the servers response
    response = s.recv(2048).decode()

    # Print the server's response
    print("Response: {}".format(response))

s.close()
