# N = int(input("Qtd: "))
# contador = 0

# while N > contador: 
#     A = str(input("A: "))
#     B = str(input("B: "))

#     A = A[-(len(B)):]
#     if A == B:
#         print("encaixa")
#     else:
#         print("nao encaixa")
#     contador +=1


# for i in range(1000): 
#     a = input()
#     b = input()
#     if len(b) > len(a): 
#         print("nao encaixa") 
#     elif a.endswith(b): 
#         print("encaixa") 
#     else: print("nao encaixa")

N = int(input())

while N > 0:
    values = input().split()


    numeros = ''
    for digit in values[0][::-1]:
        numeros += digit
        if numeros == values[1][::-1]:
            print('encaixa')
            break
    else:
        print('nao encaixa')


    numeros = ''


    N -= 1
