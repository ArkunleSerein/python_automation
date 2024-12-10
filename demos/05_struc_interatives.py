i = 0

while i < 10:
    i += 1

    if  i == 3:
        print("ma variable est égale à 3")
    if  i == 2:
        continue
    if i == 7:
        break
    print(i)

print("-" * 50)

for i in range ( 0, 11):
    print(f"La valeur de i est : {i}")

for i in range(0, 11, 2):
    print(f"La valeur de i est : {i}")
