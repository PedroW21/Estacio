# Condicionais em python 
# Obs: nas condicionais não precisa usar ()
print("------------ INICIANDO ------------")
print("")

idade = int(input("Digite sua idade: "))

if(idade < 0 or idade > 120):
    print("Impossível existir essa idade! Fale a verdade!")

elif(idade >= 0 and idade <= 10):
    print("Você é uma criança ou bebezinho")

elif(idade > 10 and idade < 18):
    print("Você é um adolescente")

elif(idade >= 18 and idade < 60):
    print("Você é um adulto")

else:
    print("Você é um idoso")

print("")
print("------------ FIM ------------")
