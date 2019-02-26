# Learning to count the letters in a sequence from a file
f = open("dna.txt", "r")
seq = f.read()
f.close()

seq = seq.replace("\n", "").replace(" ", "")
total_lenght = len(seq)

num_A = seq.count("A")
num_C = seq.count("C")
num_G = seq.count("G")
num_T = seq.count("T")

print("The total lenght of the sequence is:", total_lenght)
print("The character A appears ", num_A, "times")
print("The character C appears", num_C, "times")
print("The chatacter G appears", num_G, "times")
print("The character T appears", num_T, "times")
