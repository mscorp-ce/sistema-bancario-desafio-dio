from model.repository.conta_corrente_repository import ContaCorrenteRepository

class ContaCorrenteService:
    def __init__(self, conta_corrente, contas):
        self.conta_corrente = conta_corrente
        self.contas = contas
        self.repository = ContaCorrenteRepository(self.conta_corrente, self.contas)

    def garvar(self, conta_corrente):
        return self.repository.garvar(conta_corrente)
