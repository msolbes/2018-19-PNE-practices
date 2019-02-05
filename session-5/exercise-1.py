ef count_a(seq):
    """Computing the number of As in the sequence"""
    result_a = 0
    result_c = 0
    result_g = 0
    result_t = 0

    for b in seq:
        if b == 'A':
            result_a += 1

        elif b == 'C':
            result_g +=1

        elif b == 'G':
            result_g +=1
        elif b == 'T':
            result_t +=1


    return result
#Main program
s = input("please enter the sequence: ")
na = count_a(s)
print("The number of As is: {}".format(na))

#Calculate the total sequence length
tl = len(s)

#Calculate the percentage of As in the sequence
if tl > 0:
    perc = round(100.0 * na/tl,1)

else:
    perc = 0

print("The total lenght is: {}".format(tl))
print("The percentage of As is