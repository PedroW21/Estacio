class Pessoa:
    "Classe base para uma Pessoa" # Representa e faz uma documentação da classe

    contador = 0

    def __init__(self,nome,idade): #Metodo construtor em python
        self.nome = nome
        self.idade = idade
        Pessoa.contador +=1
    
    def mostraQtd(self):
        print("Número de Pessoas: %d", Pessoa.contador)

    def mostraPessoa(self):
        print("Nome:", self.nome, "| Idade:", self.idade)

pessoa1 = Pessoa("Pedro", 19)
pessoa2 = Pessoa("Victor", 18)

pessoa1.mostraPessoa()
#print(pessoa1.idade)

#print(pessoa2.nome)
#print(pessoa2.idade)