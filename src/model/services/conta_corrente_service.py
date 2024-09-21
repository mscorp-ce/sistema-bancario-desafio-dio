from model.repository.conta_corrente_repository import ContaCorrenteRepository

class ContaCorrenteService:
    def __init__(self, conta_corrente, contas):
        self.conta_corrente = conta_corrente
        self.contas = contas
        self.repository = ContaCorrenteRepository(self.conta_corrente, self.contas)


    def garvar(self, conta_corrente):
        return self.repository.garvar(conta_corrente)
        

    def validar_transacoes(self, conta): 
        numero_transacoes_no_dia = len(conta.movimentacoes.filtrar_transacoes_por_dia())

        if  numero_transacoes_no_dia == 10:
            print("\nO número máximo de transações permitidas no dia foi excedido.")
            return
        
        return numero_transacoes_no_dia


    def depositar(self, conta, transacao):
        if transacao.valor > 0:
           
           retorno = self.validar_transacoes(conta)

           if retorno is None:
               return

           return self.repository.depositar(conta, transacao)
        else:
            print("\nO valor informado é inválido. Informe um valor maior do que zero.")
            return False


    def sacar(self, conta, transacao):
        if transacao.valor > 0:
            retorno = self.validar_transacoes(conta)

            if retorno is None:
                return

            if transacao.valor > conta.saldo:
                print("\nSaldo insuficiente.")
                return False
                
            return self.repository.sacar(conta, transacao)
        else:
            print("\nO valor informado é inválido. Inform um valor maior do que zero.")
            return False