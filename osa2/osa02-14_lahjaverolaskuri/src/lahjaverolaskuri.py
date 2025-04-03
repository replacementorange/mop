maara = int(input("Lahjan suuruus? "))

if maara >= 1000000:
    maksettava = float(142100 + (maara-1000000) * 0.17)
    print(f"Vero: {maksettava} euroa")
elif maara < 1000000 and maara >= 200000:
    maksettava = float(22100 + (maara-200000) * 0.15)
    print(f"Vero: {maksettava} euroa")
elif maara < 200000 and maara >= 55000:
    maksettava = float(4700 + (maara-55000) * 0.12)
    print(f"Vero: {maksettava} euroa")
elif maara < 55000 and maara >= 25000:
    maksettava = float(1700 + (maara-25000) * 0.10)
    print(f"Vero: {maksettava} euroa")
elif maara <= 25000 and maara >= 5000:
    maksettava = float(100 + (maara-5000) * 0.08)
    print(f"Vero: {maksettava} euroa")
else:
    print("Ei veroa!")