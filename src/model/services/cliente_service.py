from model.repository.cliente_repository import ClienteRepository
from model.entities.cliente import Cliente

class ClienteService:
    def __init__(self, cliente, clientes):
        self.cliente = cliente
        self.clientes = clientes

    def consultar(self):
         cpf = self.cliente.cpf
         repository = ClienteRepository(cpf, self.clientes)

         cliente = repository.consultar()
             
         return cliente

    def garvar(self, cliente):

        cliente_cadastrado = self.consultar()

        if cliente_cadastrado:
             raise Exception("\nJá existe cliente com esse CPF!")
        
        repository = ClienteRepository(self.cliente.cpf, self.clientes)

        return repository.garvar(cliente)
