import os

def menu():
    escolha = 0
    while(escolha != 5):
        print("\n1 - Adição | 2 - Subtração | 3 - Divisão | 4 - Multiplicação | 5 - Sair")
        escolha = int(input("Faça sua escolha: "))

        if(escolha == 1):
            (op1,op2) = entrada_dados()
            resultado = adicao(op1, op2)
        elif escolha == 2:
            (op1,op2)=entrada_dados()
            resultado = subtracao(op1,op2)
        elif escolha == 3:
            (op1,op2)=entrada_dados()
            resultado = divisao(op1,op2)
        elif escolha == 4:
            (op1,op2)=entrada_dados()
            resultado = multiplicacao(op1,op2)
        elif escolha==5:
            finalizar()

        print("O resultado é: ",resultado)

# Dados par a realizar a operação desejada
def entrada_dados():
    operando1 = float(input("Operando 1: "))
    operando2 = float(input("Operando 2: "))
    return operando1, operando2

# Operações

def adicao(op1,op2):
    os.system("cls") # limpa a tela
    print("*** ADIÇÃO ***")
    resultado = op1 + op2
    return resultado

def subtracao(op1,op2):
    os.system("cls")
    print("*** SUBTRAÇÃO ***")
    resultado = op1 - op2
    return resultado

def multiplicacao(op1,op2):
    os.system("cls")
    print("*** MULTIPLICAÇÃO ***")
    resultado = op1 * op2
    return resultado

def divisao(op1,op2):
    os.system("cls")
    print("*** DIVISÃO ***")    
    resultado = op1 / op2
    return resultado

def finalizar():
    print("\n Bye Bye! \n")
    quit()

menu()