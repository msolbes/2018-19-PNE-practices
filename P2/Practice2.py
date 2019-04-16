import socket
from P1.Seq import Seq
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 1114
IP = "158.42.240.34"

condition = True
while True:

    sequence = Seq(input("Please enter a valid sequence: ").upper())
    complement_seq = sequence.complement()
    reverse_seq = sequence.reverse()

    s.connect((IP, PORT))
    s.send(str.encode("The complement of the sequence is: {}".format(complement_seq)))
    s.send(str.encode("\tThe reverse of the sequence is: {}".format(reverse_seq)))

    msg = s.recv(2048).decode("utf-8")
    print("\nMessage from the server:")
    print(msg)

    s.close()
