
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

def novo_titutlar():
    pass

def nova_conta():
    print("Nova conta")

def depositar():
    print("Depositar")
    
def sacar():
    print("Sacar")

def extrato():
    print("Extrato")

def main():
    while True:
        opcao = input(menu())

        if opcao == "d":
            depositar()
        elif opcao == "s":
            sacar()
        elif opcao == "e":
            extrato()
        elif opcao == "t":
            novo_titutlar()
        elif opcao == "n":
            nova_conta()
        elif opcao == "q":
            print("Sair")
            break  
        else:
            print("Opção inválida. Tente novamente.")  

if __name__ == "__main__":
    main()
