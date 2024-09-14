from model.services.cliente_service import ClienteService
from model.entities.cliente import Cliente

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

    service = ClienteService(cpf, clientes)

    try:
        cliente = service.consultar()

        if cliente == None:
           cliente = Cliente(nome, cpf)
           clientes.append(cliente)
    
    except Exception as erro:
        print("Erro:" + str(erro))

def nova_conta():
    print("Nova conta")

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
            nova_conta()
        elif opcao == "q":
            print("Sair")
            break  
        else:
            print("Opção inválida. Tente novamente.")  

if __name__ == "__main__":
    main()
