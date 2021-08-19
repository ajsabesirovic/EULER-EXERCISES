el1 = 1
el2 = 2
sum = 0

while el2 < 4000000:
    if el2 % 2 == 0:
        sum += el2
    pom = el1
    el1 = el2
    el2 = pom + el1

print(sum)



