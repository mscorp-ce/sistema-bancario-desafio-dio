from datetime import datetime
import uuid

class Movimentacoes:
    def __init__(self):
        self.transacoes = []

    def efeturar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tid:": uuid.uuid4(),
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )