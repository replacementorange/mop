salasana = str(input("Salasana: "))
toista_salasana = str(input("Toista salasana: "))

while True:
    if salasana == toista_salasana:
        print("Käyttäjätunnus luotu!")
        break
    else:
        print("Ei ollut sama!")
        toista_salasana = str(input("Toista salasana: "))