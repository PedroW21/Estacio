import random # posso usar o metodo .shuffle() para bagunçar os elementos da lista

lista = ["Isso", "é", 1, "lista"] # listas podem guardar objts e isso que as diferenciam de um array (e também varios tipos de dados em si mesma)

print("\nVerificando se a lista contem um elemento")
print(1 in lista)
print("Pierre" in lista)

print("\nVerificando o minimo, o maximo e a soma dos numeros de uma lista")
numeros = [1,128,12,356,0,888]

print(min(numeros))
print("")

print(max(numeros))
print("")

print(sum(numeros))


print("")
print("Colocando elementos no final da lista")

estados = ["TO, GO"]
print("Lista original:", estados)

estados.append("DF") # no final da lista

print("Lista modificada:", estados)


print("\nRemovendo o elemento do final da lista (ou posição escolhida pelo paramentro)")
estados.append("SP")

print("Lista com mais um estado indevido:", estados)
estados.pop()
print("Lista modificada:", estados)


print("\nRemovendo um elemento sem saber sua localização")
pessoas = ["Pedro", "Joaquina", "Mariazinha", "Tico", "Teco", "Iriney", "Tadeu Comeu"]
print("Lista original:", pessoas)

pessoas.remove("Tadeu Comeu")

print("Alteração:", pessoas)


print("\nColocando elementos em uma posição especifica")
print("Lista antes da inserção do nome: ", pessoas)

pessoas.insert(3, "Inspetor bujiganga")

print("Lista alterada:", pessoas)

print("\nOrganizando uma lista em ordem crescente e decrescente")
print("Lista de numeros desordenados:", numeros)

numeros.sort()
print("Numeros ordenados (menor pro maior):", numeros)

numeros.reverse()
print("Numeros ordenados (maior pro menor):", numeros)


print("\nContando um numero de repetições de um elemento em uma lista")
festa = ["Bolo", "Refri", "Salgadinhos", "Presentes", "Mini-games", "Jogos", "Docinhos", "Convidados", "Bolo"]

print("Lista sem modificações:", festa)

print("Qtd de bolos:",festa.count("Bolo"))

festa.append("Presentes")
festa.append("Presentes")

print("Qtd de presentes:", festa.count("Presentes"))


print("\nRetornando o indice de um elemento")
print("Indice do elemento:", festa.index("Mini-games"))


print("\nProlongando uma lista")
nordeste = ["PE", "BA", "CE", "SE", "PA"]

print("Lista de estados normal:", estados)

estados.extend(nordeste)
print("Lista de estados estendidos:", estados)
