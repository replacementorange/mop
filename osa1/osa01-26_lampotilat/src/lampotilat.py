lampotila_f = int(input("Anna lämpötila (F): "))
lampotila_c = float((lampotila_f - 32) * 5/9)
if (lampotila_c < 0):
    print(f"{lampotila_f} fahrenheit-astetta on {lampotila_c} celsius-astetta")
    print("Paleltaa!")
else:
    print(f"{lampotila_f} fahrenheit-astetta on {lampotila_c} celsius-astetta")