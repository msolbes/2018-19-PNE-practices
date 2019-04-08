# Learning the fibonacci sequence and adding its terms
nterms = int(input("How many terms would you like?: "))


def fibonacci(term):
    n1 = 0
    n2 = 1
    list_terms = []
    if nterms <= 0:
        print("Please enter a positive number")
    elif nterms == 1:
        print(n1)
    else:
        print("Fibonacci sequence with", nterms, ":")
        for i in range(term):
            list_terms.append(n1)
            n1 = n2
            n2 = n1+n2
        add = 0
        for i in list_terms:
            add = add + i
        return add


fib_series = fibonacci(nterms)
print('The final series is: ', fib_series)
