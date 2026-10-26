print("_____ FP 02 | EX 09 _____")

a = int(input("Insira um número: "))
b = int(input("Insira um número: "))
c = int(input("Insira um número: "))

if a < b < c:
    print(f"Menor: {a}")

if b < a < c:
    print(f"Menor: {b}")

if c < a < b:
    print(f"Menor: {c}")
