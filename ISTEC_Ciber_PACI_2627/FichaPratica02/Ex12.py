print("_____ FP 02 | EX 09 _____")

print("***** MENU *****")
print("1. Criar")
print("2. Atualizar")
print("3. Eliminar")
print("4. Sair")

opcao = int(input("Insira a opção: "))

if opcao == 1:
    print("Criar")
elif opcao == 2:
    print("Atualizar")
elif opcao == 3:
    print("Eliminar")
elif opcao == 4:
    print("")
else:
    print(f"Erro. Opção Inválida: {opcao}")
