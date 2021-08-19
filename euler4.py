broj = 1

while True:
    brojac = 0
    for i in range(1,21):
        if broj % i == 0:
            brojac += 1
    if brojac == 20:
        break
    broj += 1

print(broj)
print(brojac)
