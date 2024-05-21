# texto = input("Digite uma palavra: ")
texto = ""
VOGAIS = "AEIOU"

for i in texto:
    if i.upper() in VOGAIS:
        print(i, end="")
else:
    print()
    print("Executa no final do laço")


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero)
    


