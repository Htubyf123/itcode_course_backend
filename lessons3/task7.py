n = int(input("Введите число: "))
fib1 = fib2 = 1
while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1
print(fib2)
