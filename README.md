# sistema-bancario-desafio-dio

Este é um sistema de gerenciamento bancário simples, desenvolvido em Python, que permite o cadastro de clientes, criação de contas, realização de depósitos e saques, além da consulta de extratos e saldo.

Funcionalidades
Cadastro de Clientes: Permite o registro de novos titulares com nome e CPF.
Criação de Contas: Possibilita a abertura de novas contas para os clientes cadastrados.
Depósitos e Saques: Realiza operações de depósito e saque nas contas.
Consulta de Extrato: Gera um extrato das transações realizadas em uma conta.
Consulta de Saldo: Permite verificar o saldo atual da conta.

Estrutura do Código
O sistema é dividido em várias classes e funções, organizadas para facilitar a manutenção e a compreensão:

Classes de Entidades:

Cliente: Representa um cliente do banco.
ContaCorrente: Representa uma conta corrente vinculada a um cliente.
Movimentacoes: Gerencia as transações realizadas na conta.
Transacao: Classe abstrata para as transações, com subclasses Deposito e Saque.

Serviços:

ClienteService: Gerencia as operações relacionadas aos clientes.
ContaCorrenteService: Gerencia as operações relacionadas às contas correntes.

Classes utilitárias:

Format: Responsável por adiconar a mascara de formato monetário de moéda.

Funções:

menu(): Exibe o menu principal para o usuário.

novo_titutlar(): Registra um novo cliente.

nova_conta(): Cria uma nova conta para um cliente.

depositar(): Realiza um depósito na conta.

sacar(): Realiza um saque da conta.

extrato(): Exibe o extrato da conta.

saldo(): Exibe o saldo disponível na conta.

Pré-requisitos

Python 3.x

Bibliotecas:

pandas: Para manipulação de dados.

tabulate: Para exibição de dados em formato tabular.

Como Executar

Clone o repositório:

git clone https://github.com/mscorp-ce/sistema-bancario-desafio-dio.git

cd <DIRETORIO_DO_REPOSITORIO>

Instale as dependências:

pip install pandas tabulate

Execute o sistema:

python main.py

Exemplo de Uso

Ao iniciar o sistema, você verá um menu com opções. Siga as instruções na tela para cadastrar clientes, criar contas e realizar transações.

Contribuições

Sinta-se à vontade para contribuir com melhorias, correções ou novas funcionalidades. Faça um fork do projeto, implemente suas alterações e envie um pull request.

Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.