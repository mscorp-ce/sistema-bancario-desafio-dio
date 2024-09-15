

class ContaCorrenteRepository: 
    def __init__(self, conta_corrente, contas):
        self.conta_corrente = conta_corrente
        self.contas = contas

    def garvar(self, conta_corrente):

        self.contas.append(conta_corrente)

        return len(self.contas) > 0