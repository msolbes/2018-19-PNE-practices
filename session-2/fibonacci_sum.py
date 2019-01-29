def fibo(n):
    if n < 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
n=int(input("Introduce the term you wish: "))
sum = 0
for i in range(0, n):
    r = fibo(i)
    sum += r
    print(r)

print("The total addition is:", sum)