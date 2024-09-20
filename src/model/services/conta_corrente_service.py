from model.repository.conta_corrente_repository import ContaCorrenteRepository

class ContaCorrenteService:
    def __init__(self, conta_corrente, contas):
        self.conta_corrente = conta_corrente
        self.contas = contas
        self.repository = ContaCorrenteRepository(self.conta_corrente, self.contas)


    def garvar(self, conta_corrente):
        return self.repository.garvar(conta_corrente)
        

    def depositar(self, conta, transacao):
        if transacao.valor > 0:
            return self.repository.depositar(conta, transacao)
        else:
            print("\nO valor informado é inválido. Informe um valor maior do que zero.")
            return False


    def sacar(self, conta, transacao):
        if transacao.valor > 0:
            numero_saques = sum(1 for transacao in conta.movimentacoes.transacoes if transacao['tipo'] == "Saque")

            if transacao.valor > conta.saldo:
                print("\nSaldo insuficiente.")
                return False
                
            limite_excedido = transacao.valor > conta.limite
            
            saques_excedido = numero_saques >= conta.limite_saques

            if limite_excedido:
                print("\nO valor do saque excede o seu limite.")
                return False
            elif saques_excedido:
                print("\nO número máximo de saques foi excedido.")
                return False

            return self.repository.sacar(conta, transacao) # efetuar(conta, transacao)
        else:
            print("\nO valor informado é inválido. Inform um valor maior do que zero.")
            return False