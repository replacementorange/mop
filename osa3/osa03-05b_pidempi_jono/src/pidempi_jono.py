eka = input("Anna jono 1: ")
toka = input("Anna jono 2: ")

if len(eka) > len(toka):
    print(eka + " on pidempi")
elif len(eka) < len(toka):
    print(toka + " on pidempi")
else:
    print("Jonot ovat yhtä pitkät")