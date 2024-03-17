# Calculadora soma/btração/divisao/multiplicaçao

num1 = float(input("Digite um valor: "))
num2 = float(input("Digite um valor: "))

print("qual operação você deseja fazer")
print("\t 1 - Soma")
print("\t 2 - Subtração")
print("\t 3 - Multiplicação")
print("\t 4 - Divisão")

op = input("Digite o valor entre (1-4)?")

if (op == "1"):
    print(num1, "+", num2, " = ", num1 + num2)
elif(op == "2"):
    print(num1, "-", num2, " = ", num1 - num2)
elif(op == "3"):
    print(num1, "*", num2, " = ", num1 * num2)
elif(op == "4"):
    print(num1, "/", num2, " = ", num1 / num2)
else:
    print("Essa opção não existe, tente novamente ")
    