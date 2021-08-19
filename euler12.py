br = 1
triBr = 0

while True:
    triBr += br
    dividers = []
    for i in range(1,triBr+1):
        if triBr % i == 0:
            dividers.append(i)
    if len(dividers) > 500:
        print(triBr,dividers)
        break
    br += 1


