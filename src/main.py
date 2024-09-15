from model.services.cliente_service import ClienteService
from model.entities.cliente import Cliente
from model.entities.conta_corrente import ContaCorrente
from model.services.conta_corrente_service import ContaCorrenteService

def menu():
    opcoes = """\n
    |================ MENU ================|
    | [t] Novo Titular                     |
    | [n] Nova Conta                       |
    | [d] Depositar                        |
    | [s] Sacar                            |
    | [e] Extrato                          |
    | [q] Sair                             |
    |======================================|
    =>"""
    return opcoes

def novo_titutlar(clientes):
    nome = input("Informe o nome completo: ")

    cpf = input("Informe o CPF (somente número): ")

    cliente = Cliente(nome, cpf)
    try:
        service = ClienteService(cliente, clientes)

        if service.garvar(cliente):
            print("\nClientes :" + str(len(clientes)))
            print("Titular cadastrado com sucesso.")
    
    except Exception as erro:
        print("Erro: " + str(erro))

def nova_conta(clientes, contas):
    numero_conta = len(contas) + 1

    cpf = input("Informe o CPF (somente número): ")

    cliente = Cliente("", cpf)

    service = ClienteService(cliente, clientes)

    try:
        cliente = service.consultar()

        if cliente == None:
            print("Titular do CPF informado não consta em nosso cadastro..")

        conta = ContaCorrente(numero_conta, cliente)

        conta_service = ContaCorrenteService(conta, contas)

        if conta_service.garvar(conta):
            print("Nova conta cadastrada com sucesso.")
            print("Numero de contas: " + str(len(contas)))
    
    except Exception as erro:
        print("Erro:" + str(erro))    

def depositar():
    print("Depositar")
    
def sacar():
    print("Sacar")

def extrato():
    print("Extrato")

def main():
    clientes = []
    contas = []

    while True:
        opcao = input(menu())

        if opcao == "d":
            depositar()
        elif opcao == "s":
            sacar()
        elif opcao == "e":
            extrato()
        elif opcao == "t":
            novo_titutlar(clientes)
        elif opcao == "n":
            nova_conta(clientes, contas)
        elif opcao == "q":
            print("Sair")
            break  
        else:
            print("Opção inválida. Tente novamente.")  

if __name__ == "__main__":
    main()
