sumFinal = 0
for x in range(1, 10001):
    divisors = []
    divisors1 = []
    for i in range(1, x):
        if x % i == 0:
            divisors.append(i)
    y = sum(divisors)
    for i in range(1, y):
        if y % i == 0:
            divisors1.append(i)
    if sum(divisors1) == x and sum(divisors) == y and x != y and x < y:
        print(x)
        print(y)
        sumFinal += (x+y)
    x += 1
print(sumFinal)
