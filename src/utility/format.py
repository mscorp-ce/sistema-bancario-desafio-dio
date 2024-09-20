
class Format:
    def __init__(self, simbolo_moeda="R$"):
        self.simbolo_moeda = simbolo_moeda

    def moeda(self, valor):
        return f"R$ {valor:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.') 
        
 