
from model.entities.movimentacoes import Movimentacoes

class ContaCorrente:
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        self.numero = numero
        self._cliente = cliente
        self._limite = limite
        self._limite_saques = limite_saques
        self._saldo = 0
        self.movimentacoes = Movimentacoes()