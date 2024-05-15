saldo = 0
qtde_saque = 0
extrato = ""
LIMITE_QUANTIDADE_SAQUE_DIARIO = 3
LIMITE_SAQUE = 500

menu = """
[1] - Depositar
[2] - Sacar
[3] - Verificar Extrato
[0] - Sair

Opção: 
"""

while True:
    opcao = int(input(menu))
    
    if(opcao == 1):
        valor = float(input("Digite o valor do depósito: "))
        if (valor > 0):
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso!\n")
        else:
            print("Valor inválido!")    
    elif(opcao == 2):
        valor = float(input("Digite o valor do saque: "))

        valida_saldo = valor > saldo

        valida_limite_saque = valor > LIMITE_SAQUE

        valida_qtde_saque  = qtde_saque >= LIMITE_QUANTIDADE_SAQUE_DIARIO

        if valida_saldo:
            print("Saldo insuficiente!")
        elif valida_limite_saque:
            print(f"Valor do saque excede o limite de R$ {LIMITE_SAQUE:.2f}")
        elif valida_qtde_saque:
            print(f"Quantidade saque diário excedido ({LIMITE_QUANTIDADE_SAQUE_DIARIO})")
        elif valor > 0:
            saldo -= valor
            extrato +=f"Saque de R$ {valor:.2f}\n"
            qtde_saque += 1
            print("n\Saque realizado com sucesso!\n")

    elif(opcao == 3):
        print("------- EXTRATO -------")
        print("Não houve transações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("-----------------------")
    elif(opcao == 0):
        print("Obrigado por utilizar nosso serviço!")
        break
    else:
        print("Opção inválida")
