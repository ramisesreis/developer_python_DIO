opcao = -1

while opcao != 0:
    opcao = int(input("Informe um número: "))

    if opcao == 10:
        break

    print(opcao)

for numero in range(100):

    if numero %2 == 0:
        continue

    print(numero, end=" ")
