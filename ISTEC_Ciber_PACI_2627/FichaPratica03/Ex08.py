print("_____ FP 03 | EX 08 _____")

numeroUtilizador = int(input("Insira um número: "))

# 5 anteriores
numero = numeroUtilizador-5
limite = numeroUtilizador-1

while numero <= limite:
    print(numero)
    numero = numero + 1


# 5 sucessores

numero = numeroUtilizador+1
limite = numeroUtilizador+5

while numero <= limite:
    print(numero)
    numero = numero + 1