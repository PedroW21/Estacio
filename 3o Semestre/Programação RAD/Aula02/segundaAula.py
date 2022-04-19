# Meios de se quebrar linha em python

#textaoGigante = "Esse é um exemplo de textão:\n Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,\n when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.\n It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,\n and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

#textaoGigante2 = """Esse é outro exemplo de textão gigante: 
#Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
#Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
#Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
#Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
#"""

#print(textaoGigante)
#print("")
#print(textaoGigante2)

# Recebendo dados

nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
sexo = input("Qual seu sexo? ")

print("Seu nome é " + nome + " e você tem ", idade*360," dias e seu sexo é " + sexo)