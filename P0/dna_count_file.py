# Learning to count the letters in a sequence from a file
file_name = input("Name of the file")
with open(file_name, "r") as f:
    seq = ""
    for line in f:
        line = line.replace("\n", "").replace(" ", "")
        seq += line
    total_length = len(seq)
    seq = seq.upper()

    num_A = seq.count("A")
    num_C = seq.count("C")
    num_G = seq.count("G")
    num_T = seq.count("T")

    print("The total length of the sequence is:", total_length)
    print("The character A appears ", num_A, "times")
    print("The character C appears", num_C, "times")
    print("The character G appears", num_G, "times")
    print("The character T appears", num_T, "times")
