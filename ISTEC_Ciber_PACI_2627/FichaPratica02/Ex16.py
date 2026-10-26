print("_____ FP 02 | EX 16 _____")

valor = int(input("Valor a levantar: "))

if valor % 5 == 0:
    notas = valor // 200
    print(f"Notas de 200€: {notas}")
    valor = valor % 200

    notas = valor // 100
    print(f"Notas de 100€: {notas}")
    valor = valor % 100

    notas = valor // 50
    print(f"Notas de  50€: {notas}")
    valor = valor % 50

    notas = valor // 20
    print(f"Notas de  20€: {notas}")
    valor = valor % 20

    notas = valor // 10
    print(f"Notas de  10€: {notas}")
    valor = valor % 10

    notas = valor // 5
    print(f"Notas de   5€: {notas}")

else:
    print("Não damos trocos")