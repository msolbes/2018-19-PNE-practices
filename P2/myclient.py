class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        print("New empty sequence created")

        self.strbases = strbases

    def complement(self):

        seqcomp = ""

        for n in self.strbases:
            if n == "A":
                seqcomp += "T"
            elif n == "T":
                seqcomp += "A"
            elif n == "C":
                seqcomp += "G"
            elif n == "G":
                seqcomp += "C"
        return seqcomp

    def reverse(self):

        seqrev = self.strbases()

        return seqrev














str1= s1.strbases
str2= s2.strbases

import socket

PORT = 1112
IP = "212.128.253.70"

condition= True
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(seq)))

    seq = input("Please enter a valid sequence")

print("Sequence 1: {}".format(str1))
print("Sequence 2: {}".format(str2))
print("the end")