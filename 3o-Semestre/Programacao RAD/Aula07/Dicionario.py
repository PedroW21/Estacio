# Em Python, dicionário é um tipo de estrutura de dados em que há mapeamento entre uma chave (key) e um valor (value).

contatos = {}

tel_porco_aranha = ["654-321", "888-888"]
tel_iliano = ["555-555", "123-782"]

contatos["Pierre"]=["123-456"]
contatos["Adalberto"]=["263-889"]
contatos["Porco-aranha"]=tel_porco_aranha
contatos["Iliano"]=tel_iliano

print(contatos)

print("\nAcessando o Dicionário\n")

print(contatos["Iliano"])
print(contatos["Porco-aranha"])
print("")

print("Alterando o Dicionário\n")
contatos["Pierre"]=["Inexistente"]

print("Pierre:", contatos["Pierre"])

# Ordenando Dicionarios

print("\nChaves do dicionário [Contatos]:", contatos.keys()) # permite identificar o par chave do dicionario
print("")

print("Valores do dicionário [Contatos]:", contatos.values()) # permite identificar o par valores do dicionario
print("")

print("Outro meio de acessar o conteúdo de uma chave:")

print("Conteudo da chave:", contatos.get("Adalberto"))

print("")

print("Verificando se há um elemento no dicionário")

print("Tem o elemento Kaka no dicionário? ", "kaka" in contatos)
print("Tem o elemento Pierre no dicionário? ", "Pierre" in contatos)

# Retorna os elementos do Dicionário em forma de tuplas
print("")

print(contatos.items())

# Copiando o conteudo de um dicionario para outro
print("")

herois = contatos.copy()
print("Hérois:\n",herois)

# dictonary_name.clear() -> apaga todos os elementos do dicionario

#Criando o dicionário de uma forma diferente

temperaturas = dict([(1, 38), (2, 36), (3, 32)])

print("\nTemperaturas:", temperaturas)