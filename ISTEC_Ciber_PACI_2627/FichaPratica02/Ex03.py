print("_____ FP 02 | EX 03 _____")

salario = float(input("Insira o seu salário anual: "))

if salario <= 15000:
    taxa = salario * 0.2
    print(f"Taxa 20%: {taxa} €")

if salario > 15000 and salario <= 20000:
    taxa = salario * 0.3
    print(f"Taxa 30%: {taxa} €")

if salario > 20000 and salario <= 25000:
    taxa = salario * 0.35
    print(f"Taxa 35%: {taxa} €")

if salario > 25000:
    taxa = salario * 0.4
    print(f"Taxa 40%: {taxa} €")
