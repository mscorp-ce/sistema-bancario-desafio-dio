
class ClienteRepository:
    def __init__(self, cliente, clientes):
        self.cliente = cliente
        self.clientes = clientes

    def consultar(self):
        clientes_filtrados = [cliente for cliente in self.clientes if cliente.cpf == self.cliente.cpf]

        return clientes_filtrados[0] if clientes_filtrados else None
    
    def garvar(self, cliente):

        self.clientes.append(cliente)

        return len(self.clientes) > 0