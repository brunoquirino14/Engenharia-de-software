print("O que deseja fazer?")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

value = int(input("Escolha uma opção: "))  # Converte para inteiro

print("Escreva o primeiro número da operação: ")
primeiro = int(input())  # Converte para inteiro

print("Escreva o segundo número da operação: ")
segundo = int(input())  # Converte para inteiro

if value == 1:
    print(primeiro + segundo)
elif value == 2:
    print(primeiro - segundo)
elif value == 3:
    print(primeiro * segundo)
elif value == 4:
    if segundo != 0:  # Evita divisão por zero
        print(primeiro / segundo)
    else:
        print("Erro: divisão por zero!")
else:
    print("Número não existe!")
