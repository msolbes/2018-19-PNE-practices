import http.client
import json
import termcolor
from P7.Sequence import Seq

PORT = 8003
SERVER = 'http://rest.ensembl.org/'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

r1 = conn.getresponse()

print("Response received!: {} {}\n".format(r1.status, r1.reason))

data1 = r1.read().decode("utf-8")

data = json.loads(data1)

seq = data["seq"

sequence = Seq(seq)

number1 = len(sequence)

number2 = 0
for a in sequence:
    if a == "T":
        number2 = number2 + 1
number_bases = count(sequence)

list_max =
max_number = max(list_max, key=int)
