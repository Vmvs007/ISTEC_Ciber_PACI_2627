print("_____ FP 01 | EX 06 _____")

# 1. Perguntar os valores ao utilizador
valor1 = int(input("Insira o 1º valor: "))
valor2 = int(input("Insira o 2º valor: "))

# 2. Trocar os valores
valor1 = valor1 + valor2
valor2 = valor1 - valor2
valor1 = valor1 - valor2

# 3. Apresentar os valores
print(f"\nValor 1: {valor1}")
print(f"Valor 2: {valor2}")
