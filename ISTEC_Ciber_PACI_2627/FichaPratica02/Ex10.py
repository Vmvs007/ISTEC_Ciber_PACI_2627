print("_____ FP 02 | EX 10 _____")

num1 = float(input("Insira o 1º número: "))
num2 = float(input("Insira o 2º número: "))

operacao = input("Operação aritmética ( + - * / ): ")

if operacao == "+":
    soma = num1 + num2
    print(f"Soma: {soma}")

elif operacao == "-":
    subtracao = num1 - num2
    print(f"Subtração: {subtracao}")

elif operacao == "*":
    multi = num1 * num2
    print(f"Multiplicação: {multi}")

elif operacao == "/":
    div = num1 / num2
    print(f"Divisão: {div}")

else:
    print(f"Erro: {operacao} não reconhecido")

print("FIM")