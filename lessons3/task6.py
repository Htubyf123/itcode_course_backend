a = int(input("Введите число: "))
k = 0
for i in range(2, a):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Число простое")
else:
    print("Число составное")