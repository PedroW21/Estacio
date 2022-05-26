class Fila(object):
    def __init__(self):
        self.dados = []

    def enqueue(self, elemento):
        dados.append(elemento)

    def dequeue(self):
        dados.pop(0)

    def vazia(self):
        return len(self.dados) == 0