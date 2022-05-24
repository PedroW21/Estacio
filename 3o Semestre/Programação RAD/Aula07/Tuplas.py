# Tuplas são basicamente listas imutaveis

exemplo_tupla = ("Oi", "isso", "é", "uma", "tupla")

# Meios para acessar seus elementos

print(exemplo_tupla[0]) 

# " : " metodo com o nome de slice
print(exemplo_tupla[1:]) # todos os elementos apartir do primeiro
print(exemplo_tupla[:3]) # os primeiros 3 elementos
print(exemplo_tupla[:]) # toda tupla

# Tamanho de uma tupla

print(f"Essa tupla contém {len(exemplo_tupla)} elementos")

# Concatenando tuplas

tupla2 = ("", "Legal", "né", "=)")

print("\nContatenando Tuplas")
print(exemplo_tupla + tupla2)


oi_repetido = ('oi',) # tem que ter o diabo da " , " pois se não  o python pensará que é uma string entre aspas e não uma tupla
oi_repetido*10

print("\nTupla com repetição de um elemento em 10x:\n", oi_repetido)