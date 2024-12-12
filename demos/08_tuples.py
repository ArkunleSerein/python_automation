def test_tuple():
    return ("Valeur1", "Valeur2", "Valeur3") # tuple packing -> On se sert d'un tuple pour retourner plusieurs valeurs

print(test_tuple())

# Unpacking -> on 'découpe' notre tuple en plusieurs variables.
var1, var2, var3 = test_tuple()

print("var1", var1)
print("var2", var2)
print("var3", var3)

# La variable underscore dans python sert à se débarasser de valeurs inutiles
for _ in range(0, 10):
    print("test")

var1, _, var3 = test_tuple()

# Ici, j'inverse la valeur de var1 et var3
var1, var3 = var3, var1