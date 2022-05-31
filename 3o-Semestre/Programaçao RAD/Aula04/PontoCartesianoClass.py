class PlanoCartesiano:
    "Classe para representar um ponto cartersiano"

    def __init__(self, _pontox, _pontoy):
        self._pontox = _pontox
        self._pontoy = _pontoy
    
    def MostraPontos(self):
        print("O ponto está localizado no plano cartesiano nas seguintes coodernadas: X:", self._pontox, "| Y:", self._pontoy)

pontoP = PlanoCartesiano(312,215)
pontoQ = PlanoCartesiano(560, 870)

pontoP.MostraPontos();
