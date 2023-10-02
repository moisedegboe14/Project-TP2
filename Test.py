import unittest

def affiche():
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if not output:
            output = i  # Si ce n'est ni un multiple de 3 ni de 5, affiche simplement le nombre
        print(output)

# Appel de la méthode pour afficher les résultats
affiche()
