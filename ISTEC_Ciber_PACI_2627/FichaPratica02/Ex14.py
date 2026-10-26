print("_____ FP 02 | EX 14 _____")

a = int(input("Insira um número: "))
b = int(input("Insira um número: "))
c = int(input("Insira um número: "))

# A B C
if a < b < c:
    print(f"{a} {b} {c}")

# A C B
if a < c < b:
    print(f"{a} {c} {b}")

# B A C
if b < a < c:
    print(f"{b} {a} {c}")

# B C A
if b < c < a:
    print(f"{b} {c} {a}")

# C A B
if c < a < b:
    print(f"{c} {a} {b}")

# C B A
if c < b < a:
    print(f"{c} {b} {a}")
