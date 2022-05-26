class Contato:
    todosContatosCriados = []

    def __init__(self, nome, email): 
        self.nome = nome
        self.email = email

        Contato.todosContatosCriados.append(self) #todos os filhos que forem criados serão armazenados
    
    def mostraConteudo(self):
        print(f"Nome: {self.nome} | Email: {self.email}",) #f = format(), interpolação no print mais facilitada

class Fornecedor(Contato): 

    def pedido(self, pedido):
        print("Pedido: {0} feito por {0}", format(pedido,self.nome))

class Amigo(Contato):
    def __init__(self, nome, email, tel): 

        super().__init__(nome,email) # primeiro sera chamado o construtor da superclass (classe pai - contato) e somente depois o filho
        self.tel = tel #metodo foi sobrecarregado
    


pessoa = Contato("Pedro", "pdo@pdo.com")
empresa = Fornecedor("Werner", "wrr@wrr.com")

pessoa.mostraConteudo()
empresa.mostraConteudo()