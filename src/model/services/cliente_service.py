from model.repository.cliente_repository import ClienteRepository

class ClienteService:
    def __init__(self, cliente, clientes):
        self.cliente = cliente
        self.clientes = clientes
        self.repository = ClienteRepository(self.cliente, self.clientes)


    def consultar(self):      
         cliente = self.repository.consultar()
             
         return cliente
    

    def garvar(self, cliente):
        cliente_cadastrado = self.consultar()

        if cliente_cadastrado:
             raise Exception("Já existe cliente com esse CPF!")
        
        return self.repository.garvar(cliente)