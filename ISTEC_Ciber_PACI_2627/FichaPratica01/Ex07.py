print("_____ FP 01 | EX 07 _____")

# 1. Perguntar os valores ao utilizador
preco1 = float(input("Insira o preço do 1º produto: "))
preco2 = float(input("Insira o preço do 2º produto: "))
preco3 = float(input("Insira o preço do 3º produto: "))

# 2. Calcular o valor total
total = preco1 + preco2 + preco3

# 3. Aplicar o desconto
precoDesconto = total * 0.9

# 4. Apresentar os resultados
print(f"Preço com 10% de desconto: {precoDesconto}")
