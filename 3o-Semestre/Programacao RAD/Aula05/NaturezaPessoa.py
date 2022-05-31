class Pessoa:

    def __init__(self, nome, idade):
        
        self.nome = nome
        self.idade = idade

    def getIdade(self):
        return self.idade

class PessoaFisica(Pessoa):

    def __init__(self, nome, idade, cpf):
        
        Pessoa.__init__(self, nome, idade)
        
        self.cpf = cpf

class PessoaJuridica(Pessoa):

    def __init__(self, nome, idade, cnpj):
        
        Pessoa.__init__(self, nome, idade)
        
        self.cnpj = cnpj


pf = PessoaFisica(nome="Pierre", idade=19, cpf=123456789)
pj = PessoaJuridica(nome="Werner", idade=150, cnpj=9876543210001)
