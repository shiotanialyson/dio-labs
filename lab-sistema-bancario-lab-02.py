def menu():
    menu = """
    [1] - Depositar
    [2] - Sacar
    [3] - Verificar Extrato
    [4] - Cadastrar Usuário
    [5] - Criar Conta
    [6] - Listar Usuários
    [7] - Listar Contas
    [0] - Sair

    Opção: 
    """
    return int(input(menu))

def depositar(saldo, valor, extrato, /):
    if (valor > 0):
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!\n")
    else:
        print("Valor inválido!")    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite_qtde_saque_diario, qtde_saque, limite_saque):

    valida_saldo = valor > saldo

    valida_limite_saque = valor > limite_saque

    valida_qtde_saque  = qtde_saque >= limite_qtde_saque_diario
    print(qtde_saque)
    print(limite_qtde_saque_diario)

    if valida_saldo:
        print("Saldo insuficiente!")
    elif valida_limite_saque:
        print(f"Valor do saque excede o limite de R$ {limite_saque:.2f}")
    elif valida_qtde_saque:
        print(f"Quantidade saque diário excedido ({limite_qtde_saque_diario})")
    elif valor > 0:
        saldo -= valor
        extrato +=f"Saque de R$ {valor:.2f}\n"
        qtde_saque += 1
        print("\nSaque realizado com sucesso!\n")

    return saldo, extrato, qtde_saque

def verificar_extrato(saldo,/, *, extrato):
    print("------- EXTRATO -------")
    print("Não houve transações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("-----------------------")
    return extrato

def verificar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario

def cadastrar_usuario(usuarios):
    cpf = input("Digite o CPF: ")
    if verificar_usuario(cpf, usuarios):
        print("\nUsuário já cadastrado!\n")
        return
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Digite o endereço (logradouro, numero - bairro - cidade/sigla estado): ")
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("\nUsuário cadastrado com sucesso!\n")

def criar_conta(contas, usuarios, agencia):
    cpf = input("Digite o CPF do cliente: ")
    usuario = verificar_usuario(cpf, usuarios)
    if usuario:
        conta = {
            "usuario": usuario,
            "agencia": agencia,
            "numero": len(contas) + 1
        }
        contas.append(conta)
        print("\nConta criada com sucesso!\n")
    else:
        print("\nUsuário não cadastrado!\n")

def listar_usuarios(usuarios):
    if not usuarios:
        print("Sem cliente cadastrado")
    else:
        print("Clientes cadastrados: \n")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}\nCPF: {usuario['cpf']}\nNascimento: {usuario['data_nascimento']}\nEndereço: {usuario['endereco']}\n")

def listar_contas(contas):
    if not contas:
        print("Sem conta aberta")
    else:
        print("Contas abertas:\n")
        for conta in contas:
            print(f"Nome: {conta['usuario']['nome']}\nCPF: {conta['usuario']['cpf']}\nAgência: {conta['agencia']}\nNúmero: {conta['numero']}\n")

def main():
    saldo = 0
    qtde_saque = 0
    extrato = ""
    usuarios=[]
    contas=[]
    LIMITE_QUANTIDADE_SAQUE_DIARIO = 3
    LIMITE_SAQUE = 500
    AGENCIA = "0001"

    while True:
        opcao = menu()
        
        if(opcao == 1):
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif(opcao == 2):
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, qtde_saque = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_qtde_saque_diario=LIMITE_QUANTIDADE_SAQUE_DIARIO,
                qtde_saque=qtde_saque,
                limite_saque=LIMITE_SAQUE
            )

        elif(opcao == 3):
            extrato = verificar_extrato(saldo, extrato=extrato)
            
        elif(opcao == 4):
            cadastrar_usuario(usuarios)

        elif(opcao == 5):
            criar_conta(contas, usuarios, AGENCIA)

        elif(opcao == 6):
            listar_usuarios(usuarios)
        
        elif(opcao == 7):
            listar_contas(contas)

        elif(opcao == 0):
            print("Obrigado por utilizar nosso serviço!")
            break
        else:
            print("Opção inválida")

main()
