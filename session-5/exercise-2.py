def count_let(seq):
    """Computing the number of As in the sequence"""
    result_a = 0
    result_c = 0
    result_g = 0
    result_t = 0

    for b in seq:
        if b == 'A':
            result_a += 1
        elif b == 'C':
            result_c +=1
        elif b == 'G':
            result_g +=1
        elif b == 'T':
            result_t +=1

        dic = {"As": result_a, "Cs": result_c, "Gs": result_g, "Ts": result_t}
    return dic

#Main program
s1 = input("please enter the sequence: ").upper()
s2 = input("please enter the second sequence: ").upper()
n1_let = count_let(s1)
n2_let = count_let(s2)
print("The letters of the sequence 1 are: {}".format(n1_let))
print("The letters of the sequence 2 are: {}".format(n2_let))
#Calculate the total sequence length
tl1 = len(s1)
tl2 = len(s2)
#Calculate the percentage of As in the sequence
if (tl1 and tl2) > 0:
    perc_a1 = round(100.0 * n1_let['As'] / tl1, 1)
    perc_c1 = round(100.0 * n1_let['Cs'] / tl1, 1)
    perc_g1 = round(100.0 * n1_let['Gs'] / tl1, 1)
    perc_t1 = round(100.0 * n1_let['Ts'] / tl1, 1)

    perc_a2 = round(100.0 * n2_let['As'] / tl2, 1)
    perc_c2 = round(100.0 * n2_let['Cs'] / tl2, 1)
    perc_g2 = round(100.0 * n2_let['Gs'] / tl2, 1)
    perc_t2 = round(100.0 * n2_let['Ts'] / tl2, 1)
else:
    perc_a1 = 0
    perc_c1 = 0
    perc_g1 = 0
    perc_t1 = 0
    perc_a2 = 0
    perc_c2 = 0
    perc_g2 = 0
    perc_t2 = 0

print("The total lenght of the first sequence is: {}".format(tl1))
print("The total lenght of the second sequence is: {}".format(tl2))
print("The percentage of As is in the first sequence is : {}%".format(perc_a1))
print("The percentage of Cs is in the first sequence is : {}%".format(perc_c1))
print("The percentage of Gs is in the first sequence is : {}%".format(perc_g1))
print("The percentage of Ts is in the first sequence is : {}%".format(perc_t1))
print("The percentage of As is in the second sequence is : {}%".format(perc_a2))
print("The percentage of Cs is in the second sequence is : {}%".format(perc_c2))
print("The percentage of Gs is in the second sequence is : {}%".format(perc_g2))
print("The percentage of Ts is in the second sequence is : {}%".format(perc_t2))