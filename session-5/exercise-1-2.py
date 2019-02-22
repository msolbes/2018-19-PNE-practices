from Bases import count_let

# Main program
s = input("please enter the sequence: ").upper()
n_let = count_let(s)
print("The letters of the sequence are: {}".format(n_let))

# Calculate the total sequence length
tl = len(s)

# Calculate the percentage of As in the sequence
if tl > 0:
    perc_a = round(100.0 * n_let['As'] / tl, 1)
    perc_c = round(100.0 * n_let['Cs'] / tl, 1)
    perc_g = round(100.0 * n_let['Gs'] / tl, 1)
    perc_t = round(100.0 * n_let['Ts'] / tl, 1)

else:
    perc_a = 0
    perc_c = 0
    perc_g = 0
    perc_t = 0


print("The total lenght is: {}".format(tl))
print("The percentage of As is : {}%".format(perc_a))
print("The percentage of Cs is : {}%".format(perc_c))
print("The percentage of Gs is : {}%".format(perc_g))
print("The percentage of Ts is : {}%".format(perc_t))
