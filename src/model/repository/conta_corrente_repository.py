
class ContaCorrenteRepository: 
    def __init__(self, conta_corrente, contas):
        self.conta_corrente = conta_corrente
        self.contas = contas


    def garvar(self, conta_corrente):

        self.contas.append(conta_corrente)

        return len(self.contas) > 0

    
    def depositar(self, conta, transacao):
        saldo = conta.saldo

        conta.saldo += transacao.valor
            
        return saldo < conta.saldo


    def sacar(self, conta, transacao):
        saldo = conta.saldo

        conta.saldo -= transacao.valor
        
        return saldo > conta.saldo
            
            
    def conta(self):
        return self.contas[0]