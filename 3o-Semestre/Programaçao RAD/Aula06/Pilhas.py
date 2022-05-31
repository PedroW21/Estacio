# class Pilha:
#    "Classe pra inserção, vizualização e remoção de elementos de uma pilha"
#
#    pilha = []
#    pilha.insert(0,1)
#
#    def __init__(self):
#        self.posicao = 0
#        self.elemento = elemento
#
#    def insereElemento(elemento):
#        pilha.insert(posicao, elemento)
#
#    def removeElemento(self):
#        pilha.pop(0)

#pilha1 = Pilha()
# print(pilha1.pilha)

# pilha1.insereElemento(2)
# print(pilha1.pilha)

class Pilha(object):
    def __init__(self):
        self.dados = []

    def push(self, elemento):
        dados.insert(0, elemento)

    def pop(self):
        dados.pop(0)
