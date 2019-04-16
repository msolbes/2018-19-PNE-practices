import socket

PORT = 1112
IP = "158.42.240.34"
MAX_OPEN_REQUESTS = 5

def testing(s):
    for n in s:
        if n != "A" and n != "C" and n !="T" and n !="G":
            print("ERROR")
        else:
            print("OK")
    return

def length(s):
    len_seq = len(s)
    return len_seq

def complement(s):
    seqcomp = ""
    for n in s:
        if n == "A":
            seqcomp += "T"
        elif n == "T":
            seqcomp += "A"
        elif n == "C":
            seqcomp += "G"
        elif n == "G":
            seqcomp += "C"
    return seqcomp

def reverse(s):
    seqrev = s[::-1]
    return seqrev

def countA(s):
    count_a = 0
    for n in s:
        if n == "A":
            count_a += 1
    return {'A': count_a}

def countT(s):
    count_t = 0
    for n in s:
        if n == "T":
            count_t += 1
    return {'T': count_t}

def countC(s):
    count_c = 0
    for n in s:
        if n == "C":
            count_c += 1
    return {'C': count_c}

def countG(s):
    count_g = 0
    for n in s:
        if n == "G":
            count_g += 1
    return {'G': count_g}

def percA(s):
    len_seq = len(s)
    count_a = 0
    for i in s:
        if i == "A":
            count_a += 1
    if len_seq > 0:
        per_a = round(100.0 * count_a / len_seq, 1)
    else:
        per_a = 0
    return per_a

def percT(s):
    len_seq = len(s)
    count_t = 0
    for i in s:
        if i == "T":
            count_t += 1
    if len_seq > 0:
        per_t = round(100.0 * count_t / len_seq, 1)
    else:
        per_t = 0
    return per_t

def percC(s):
    len_seq = len(s)
    count_c = 0
    for i in s:
        if i == "C":
            count_c += 1
    if len_seq > 0:
        per_c = round(100.0 * count_c / len_seq, 1)
    else:
        per_c = 0
    return per_c

def percG(s):
    len_seq = len(s)
    count_g = 0
    for i in s:
        if i == "A":
            count_g += 1

    if len_seq > 0:
        per_g = round(100.0 * count_g / len_seq, 1)
    else:
        per_g = 0
    return per_g

def process_client(cs):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    # Read client message. Decode it as a string
    msg = cs.recv(2048).decode("utf-8")
    message = msg.split("\n")

    print("Client's message: ".format(message))

    if message[0] == "":
        print("ALIVE")
    else:
        testing(message[0])
        for n in message:
            if n == "len":
                len = length(message[0])
                print("The length of the sequence is: {}".format(len))
                cs.send(str.encode(msg))
            elif n == "complement":
                comp = complement(message[0])
                print("The complement of the sequence is: {}".format(comp))
                cs.send(str.encode(msg))
            elif n == "reverse":
                rev = reverse(message[0])
                print("The reverse of the sequence is: {}".format(rev))
                cs.send(str.encode(msg))
            elif n == "countA":
                count_a = complement(message[0])
                print("The number of As in the sequence is: {}".format(count_a))
                cs.send(str.encode(msg))
            elif n == "countT":
                count_t = complement(message[0])
                print("The number of Ts in the sequence is: {}".format(count_t))
                cs.send(str.encode(msg))
            elif n == "countC":
                count_c = complement(message[0])
                print("The number of Cs in the sequence is: {}".format(count_c))
                cs.send(str.encode(msg))
            elif n == "countG":
                count_g = complement(message[0])
                print("The number of Gs in the sequence is: {}".format(count_g))
                cs.send(str.encode(msg))
            elif n == "percA":
                perc_a = complement(message[0])
                print("The percentage of As in the sequence is: {}".format(perc_a))
                cs.send(str.encode(msg))
            elif n == "percT":
                perc_t = complement(message[0])
                print("The percentage of Ts in the sequence is: {}".format(perc_t))
                cs.send(str.encode(msg))
            elif n == "percC":
                perc_c = complement(message[0])
                print("The percentage of Cs in the sequence is: {}".format(perc_c))
                cs.send(str.encode(msg))
            elif n == "percG":
                perc_g = complement(message[0])
                print("The percentafe of Gs in the sequence is: {}".format(perc_g))
                cs.send(str.encode(msg))
    # Send the msg back to the client (echo)
    # Close the socket
    cs.close()

#Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

#To listen to the client's requests
serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}". format(serversocket))

while True:

    print("Waiting for connections at: {}, {}". format(IP, PORT))
    (clientsocket, adress) = serversocket.accept()

    #-- Process the client request
    print("Attending client: {}". format(adress))

    process_client(clientsocket)
    #-- Close the socket
clientsocket.close()
