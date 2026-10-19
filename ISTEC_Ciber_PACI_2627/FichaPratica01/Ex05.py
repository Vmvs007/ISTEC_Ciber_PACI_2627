print("_____ FP 01 | EX 05 _____")

# 1. Perguntar os valores ao utilizador
nota1 = float(input("Insira a 1º nota: "))
nota2 = float(input("Insira a 2º nota: "))
nota3 = float(input("Insira a 3º nota: "))

# 2. Média aritmética
mediaAritmetica = (nota1 + nota2 + nota3) / 3

# 3. Média Ponderada
mediaPonderada = (nota1 * 0.2) + (nota2 * 0.3) + (nota3 * 0.5)

# 4. Apresentar valores
print(f"Média Aritmética: {mediaAritmetica}")
print(f"Média Ponderada: {mediaPonderada}")
