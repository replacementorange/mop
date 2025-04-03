# tee ratkaisu tänne

def palindromi(merkkijono):
    return merkkijono == merkkijono[::-1]

while True:
    merkkijono = str(input("Anna palindromi: "))
    if palindromi(merkkijono):
        print(f"{merkkijono} on palindromi!")
        break
    else:
        print("ei ollut palindromi")