import unittest

def affiche(n):
    result = []
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if not output:
            output = i
        result.append(output)
    return result

n = 100 
results = affiche(n)
for item in results:
    print(item)
