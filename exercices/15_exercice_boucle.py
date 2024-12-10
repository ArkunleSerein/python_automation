# Écrivez un algorithme qui affiche les nombres de 1 à 100. Mais pour
# les multiples de 3, affichez "Fizz" à la place du nombre, pour les
# multiples de 5, affichez "Buzz". Pour les nombres qui sont à la fois des
# multiples de 3 et de 5, affichez "FizzBuzz".

# Algorithme FizzBuzz
for i in range(1, 101):  # On parcours les nombres de 1 à 100
    if i % 3 == 0 and i % 5 == 0:  # Si le nombre est un multiple de 3 et de 5
        print("FizzBuzz")          # On affiche FizzBuzz
    elif i % 3 == 0:  # Si le nombre est un multiple de 3
        print("Fizz")  # On affiche Fizz
    elif i % 5 == 0:  # Si le nombre est un multiple de 5
        print("Buzz")  # On affiche Buzz
    else:
        print(i)  # Sinon, on affiche le nombre 
