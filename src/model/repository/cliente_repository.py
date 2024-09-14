
class ClienteRepository:
    def __init__(self, cpf, clientes):
        self.cpf = cpf
        self.clientes = clientes

    def consultar(self):
        clientes_filtrados = [cliente for cliente in self.clientes if cliente.cpf == self.cpf]

        return clientes_filtrados[0] if clientes_filtrados else None