# Fibonacci sequence and adding
def fibo(n):
    if n < 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


num = int(input("Introduce the term you wish: "))
add = 0
for i in range(0, num):
    r = fibo(i)
    add += r
    print(r)

print("The total addition is:", add)
