import random
pkn = ["k", "p", "n"]

print("Gramy w marynarzyka")
ty = input("Papier, kamień czy nożyce?\nWpisz p, k albo n: ")

komp = random.choice(pkn)
print(ty)
print(komp)

if ty == komp:
    print("No to mamy remis")
elif ty == 'n':
    if komp == 'k':
        print("Ha! Wygrałem!")
    elif komp == 'p':
        print("Wygrałeś, brawo")
elif ty == 'p':
    if komp == 'n':
        print("Ha! Wygrałem!")
    elif komp == 'k':
        print("Wygrałeś, brawo")
elif ty == 'k':
    if komp == 'p':
        print("Ha! Wygrałem!")
    elif komp == 'n':
        print("Wygrałeś, brawo")      