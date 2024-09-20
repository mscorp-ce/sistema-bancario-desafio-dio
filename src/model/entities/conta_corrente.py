
from model.entities.movimentacoes import Movimentacoes

class ContaCorrente:
    def __init__(self, numero, cliente, limite=500, limite_saques=3, sequencia_extrato=0):
        self.numero = numero
        self.cliente = cliente
        self.limite = limite
        self.limite_saques = limite_saques
        self.sequencia_extrato = sequencia_extrato
        self.saldo = 0
        self.movimentacoes = Movimentacoes()
    