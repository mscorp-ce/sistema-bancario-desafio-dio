from model.repository.cliente_repository import ClienteRepository

class ClienteService:
    def __init__(self, cpf, clientes):
        self.cpf = cpf
        self.clientes = clientes

    def consultar(self):
         repository = ClienteRepository(self.cpf, self.clientes)

         cliente = repository.consultar()

         if cliente:
             raise Exception("\nJá existe cliente com esse CPF!")
             
         return cliente
         
