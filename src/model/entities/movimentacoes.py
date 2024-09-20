from datetime import datetime, timedelta
import uuid

class Movimentacoes:
    def __init__(self):
        self.transacoes = []

    def lancar_transacao(self, tid, data, tipo, valor, saldo):
        self.transacoes.append(
            {           
                "tid": tid,
                "data": data,
                "tipo": tipo,
                "valor": valor,
                "saldo": saldo,
            }
        )

    def efeturar_transacao(self, conta_corrente, transacao):
        if len(self.transacoes) == 0:
            data = datetime.now()
            data_anterior = data - timedelta(days=1)
            
            self.lancar_transacao("-------- Sem movimetações ---------", 
                                  data_anterior.strftime("%d/%m/%Y %H:%M:%S"),
                                  " -------- ",
                                  0.00,
                                  0.00
                                  )
        
        self.lancar_transacao(uuid.uuid4(),
                              datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                              transacao.__class__.__name__,
                              transacao.valor,
                              conta_corrente.saldo
                              )