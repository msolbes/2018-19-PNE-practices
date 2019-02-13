import socket

# Create a socket for communicating with the server

print("Socket created")
condition = True

PORT = 8083

IP = "212.128.253.64"

# Connect to the server


while condition:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(input("Please enter your message: ")))

    msg = s.recv(2018).decode("utf-8")
    print("MESSAGE FROM THE SERVER")
    print(msg)
    s.close()


print("The end")
