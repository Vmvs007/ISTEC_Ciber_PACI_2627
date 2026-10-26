print("_____ FP 02 | EX 02 _____")

salario = float(input("Insira o seu salário anual: "))

if salario <= 15000:
    taxa = salario * 0.2
    print(f"Taxa 20%: {taxa} €")
else:
    taxa = salario * 0.3
    print(f"Taxa 30%: {taxa} €")
