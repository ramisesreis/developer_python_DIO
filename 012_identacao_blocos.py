def sacar(valor):
    saldo = 500

    if saldo >= valor:
        saldo -= valor
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")
        print(saldo)
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo +=valor
    print("Deposito realizado com sucesso!")
    print(saldo)  

sacar(100)
depositar(400)
