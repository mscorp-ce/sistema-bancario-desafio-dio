from model.entities.pessoa_fisica import PessoaFisica

class Cliente(PessoaFisica):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        self.contas = []
