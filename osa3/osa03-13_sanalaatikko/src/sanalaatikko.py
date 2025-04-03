# # https://www.w3schools.com/python/ref_string_center.asp
mjono = str(input("Sana: "))

leveys = 30
keski = mjono.center(int(leveys - 2))


print("*" * leveys)
print(f"*{keski}*")
print("*" * leveys)