# Programming our first client

import socket

# Create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 1234
IP = "212.128.253.70"

# Connect to the server
s.connect((IP, PORT))

s.send(str.encode("HELLO FROM MY CLIENT"))

msg = s.recv(2018).decode("utf-8")
print("MESSAGE FROM THE SERVER")
print(msg)

s.close()

print("The end")
