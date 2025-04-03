# Kirjoita ratkaisu tähän
lista = []

while True:
    print(f"Lista on nyt {lista}")
    syote = str(input("(l)isää, (p)oista vai e(x)it: "))

    if syote == "l":
        if lista:
            alkio = lista[-1] + 1
        else:
            alkio = 1
        lista.append(alkio)
    elif syote == "p":
        lista.pop()
    elif syote == "x":
        print("Moi!")
        break