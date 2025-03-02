from tabulate import tabulate
from datetime import datetime
import uuid
from utility.format import Format

from model.services.cliente_service import ClienteService
from model.entities.cliente import Cliente
from model.entities.conta_corrente import ContaCorrente
from model.services.conta_corrente_service import ContaCorrenteService
from model.entities.deposito import Deposito
from model.entities.saque import Saque


def menu():
    opcoes = """\n
    |================ MENU ================|
    | [t] Novo Titular                     |
    | [n] Nova Conta                       |
    | [d] Depositar                        |
    | [s] Sacar                            |
    | [e] Extrato                          |
    | [v] Saldo                            |
    | [q] Sair                             |
    |======================================|
    =>"""

    return opcoes


def validar_cpf(cpf):
    if not cpf.isdigit():
        return None

    return cpf


def novo_titutlar(clientes):
    nome = input("Informe o nome completo: ")

    cpf = input("Informe o CPF (somente número): ")

    cpf = validar_cpf(cpf)

    if cpf is None:
        print("CPF só deve conter números")
        return

    cliente = Cliente(nome, cpf)

    try:
        service = ClienteService(cliente, clientes)

        if service.garvar(cliente):
            print("\nNº Titular: " + str(len(clientes)))
            print("Titular cadastrado com sucesso.")

    except Exception as erro:
        print("Erro: " + str(erro))


def recuperar_cliente(clientes):
    cpf = input("Informe o CPF do titular: ")

    cpf = validar_cpf(cpf)

    if cpf is None:
        raise Exception("\nCPF inválido!")

    cliente = Cliente("", cpf)

    service = ClienteService(cliente, clientes)

    try:
        cliente = service.consultar()

        return cliente

    except Exception as erro:
        print("Erro:" + str(erro))


def obter_cliente(clientes):
    if len(clientes) == 0:
        print("Não existe titular cadastrado.")
        return None

    try:
        cliente = recuperar_cliente(clientes)
        if cliente is None:
            print("O titular do cpf informado não esta cadastrado.")
            return None

        if len(cliente.contas) == 0:
            print("Conta não cadastrada.")
            return None

        if len(cliente.contas[0].movimentacoes.transacoes) == 0:
            print("Conta não movimentada. Faça um depósito.")
            return None

        return cliente
    except Exception as erro:
        print("Erro: " + str(erro))
        return None


def nova_conta(clientes, contas):
    numero_conta = len(contas) + 1

    try:
        cliente = recuperar_cliente(clientes)

        if cliente is None:
            print("Titular do CPF informado não consta em nosso cadastro.")
            return

        conta_corente = ContaCorrente(numero_conta, cliente)

        conta_service = ContaCorrenteService(conta_corente, cliente.contas)

        if conta_service.garvar(conta_corente):
            contas.append(conta_corente)
            print("Nova conta cadastrada com sucesso.")
            print("Numero de contas: " + str(len(cliente.contas)))

    except Exception as erro:
        print("Erro:" + str(erro))


def operacao(clientes, tipo):
    try:
        cliente = recuperar_cliente(clientes)
    except Exception as erro:
        print("Erro:" + str(erro))
        return None, None

    if not cliente:
        print("\nTitular não encontrado!")
        return None, None

    valor_input = input("Informe o valor do " + tipo + ": ")

    valor_aux = valor_input

    valor_aux = valor_aux.replace('.', '')

    if not valor_aux.isdigit():
        print("O valor informado é invalido, o mesmo só deve conter números e sepador casas decimais(' . ')")
        return cliente, None

    valor = float(valor_input)

    return cliente, valor


def validar_transacao(clientes, tipo):

    if len(clientes) == 0:
        print("Não existe titular cadastrado.")
        return None

    try:
        retorno = operacao(clientes, tipo)

        if retorno is not None:
            cliente, valor = retorno
            if cliente is None:
                return None
        else:
            return None

    except Exception as erro:
        print("Erro:" + str(erro))
        return None

    if not cliente:
        print("\nTitular não encontrado!")
        return None

    if valor is None:
        return None

    if len(cliente.contas) == 0:
        print("Conta não cadastrada.")
        return None

    if not cliente.contas:
        return None

    return cliente, valor


def depositar(clientes):
    cliente = None
    valor = None

    try:
        retorno = validar_transacao(clientes, "depósito")

        if retorno is not None:
            cliente, valor = retorno
        if retorno is None or cliente is None or valor is None:
            return
    except Exception as erro:
        print("Erro:" + str(erro))
        return

    transacao = Deposito(valor)

    conta_corrente = cliente.contas[0]

    service = ContaCorrenteService(conta_corrente, cliente.contas)

    transacao_sucedida = service.depositar(conta_corrente, transacao)

    if transacao_sucedida:
        conta_corrente.movimentacoes.efeturar_transacao(conta_corrente, transacao)

        print("Depósito realizado com sucesso.")


def sacar(clientes):
    cliente = None
    valor = None

    try:
        retorno = validar_transacao(clientes, "saque")

        if retorno is not None:
            cliente, valor = retorno
        if retorno is None or cliente is None or valor is None:
            return
    except Exception as erro:
        print("Erro:" + str(erro))
        return

    transacao = Saque(valor)

    conta_corrente = cliente.contas[0]

    service = ContaCorrenteService(conta_corrente, cliente.contas)

    transacao_sucedida = service.sacar(conta_corrente, transacao)

    if transacao_sucedida:
        conta_corrente.movimentacoes.efeturar_transacao(conta_corrente, transacao)

        print("Saque realizado com sucesso.")


def formatar_historico(historico, formato):
    return [
        {
            "data": transacao["data"],
            "tipo": transacao["tipo"],
            "valor": formato.moeda(float(transacao["valor"])),
            "saldo": formato.moeda(float(transacao["saldo"])),
        }
        for transacao in historico
    ]


def extrato(clientes):
    cliente = obter_cliente(clientes)
    if cliente is None:
        return

    historico = cliente.contas[0].movimentacoes.transacoes

    formato = Format()

    historico_formatado = formatar_historico(historico, formato)

    print("\nExtrato Bancário")
    print("DIO BANCK")
    print("Data/Hora: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    cliente.contas[0].sequencia_extrato += 1

    print("Extrato N. : " + str(uuid.uuid5(uuid.NAMESPACE_DNS,
                                           str(cliente.contas[0].sequencia_extrato))))
    print("Titular: " + cliente.nome)
    print("Nº Conta: " + str(cliente.contas[0].numero))

    print(tabulate(historico_formatado, headers="keys", tablefmt="grid", showindex=False))


def saldo(clientes):
    cliente = obter_cliente(clientes)
    if cliente is None:
        return

    historico = cliente.contas[0].movimentacoes.transacoes
    valor_saldo = sum(
        transacao['valor'] if transacao['tipo'] == "Deposito" else -transacao['valor']

        for transacao in historico
    )

    formato = Format()

    print("Saldo disponível: " + str(formato.moeda(valor_saldo)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = input(menu())

        if opcao.lower() == "d":
            depositar(clientes)
        elif opcao.lower() == "s":
            sacar(clientes)
        elif opcao.lower() == "e":
            extrato(clientes)
        elif opcao.lower() == "v":
            saldo(clientes)
        elif opcao.lower() == "t":
            novo_titutlar(clientes)
        elif opcao.lower() == "n":
            nova_conta(clientes, contas)
        elif opcao.lower() == "q":
            print("Sair")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()