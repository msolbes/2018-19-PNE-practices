import socket

PORT = 1112
IP = "158.42.240.34"
# Maximum number of clients that can connect to this server
MAX_OPEN_REQUEST = 5


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

    #ECHO SERVER
    #Reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    message = msg.split("\n")

    print("Message from the client: {}". format(message))

    if message[0] == "":
        print("ALIVE")
    else:
        testing(message[0])
        for x in message:
            if x == "len":
                len = length(message[0])
                print("The length of the sequence is: {}".format(len))
                cs.send(str.encode(msg))
            elif x == "complement":
                comp = complement(message[0])
                print("The complement of the sequence is: {}".format(comp))
                cs.send(str.encode(msg))
            elif x == "reverse":
                rev = reverse(message[0])
                print("The reverse of the sequence is: {}".format(rev))
                cs.send(str.encode(msg))
            elif x == "countA":
                count = count_A(message[0])
                print("The number of A bases in the sequence is: {}".format(count))
                cs.send(str.encode(msg))
            elif x == "countT":
                count = count_T(message[0])
                print("The number of T bases in the sequence is: {}".format(count))
                cs.send(str.encode(msg))
            elif x == "countC":
                count = count_C(message[0])
                print("The number of C bases in the sequence is: {}".format(count))
                cs.send(str.encode(msg))
            elif x == "countG":
                count = count_G(message[0])
                print("The number of G bases in the sequence is: {}".format(count))
                cs.send(str.encode(msg))
            elif x == "percA":
                perc = perc_A(message[0])
                print("The percentage of A bases in the sequence is: {}".format(perc))
                cs.send(str.encode(msg))
            elif x == "percT":
                perc = perc_T(message[0])
                print("The percentage of T bases in the sequence is: {}".format(perc))
                cs.send(str.encode(msg))
            elif x == "percC":
                perc = perc_C(message[0])
                print("The percentage of C bases in the sequence is: {}".format(perc))
                cs.send(str.encode(msg))
            elif x == "percG":
                perc = perc_G(message[0])
                print("The percentage of G bases in the sequence is: {}".format(perc))
                cs.send(str.encode(msg))
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
