menu = """
|||||||||||||||||||||||||||||||||||
||===>>[D]<<==DEPOSITAR==========||
||===>>[S]<<====SACAR============||
||===>>[E]<<===EXTRATO===========||
||===>>[Q]<<=====SAIR============||
|||||||||||||||||||||||||||||||||||
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor do DEPÓSITO: "))
        if valor > 0:
            saldo += valor
            extrato += f"\nDEPÓSITO: R$ {valor:.2f}"

        else:
            print(f"Erro no depósito! Valor: {valor} inválido.")
    elif opcao == "S":
        valor = float(input("Informe o valor do SAQUE: "))
        if saldo < valor:
            print("Erro! Saldo insuficiente.")

        elif limite < valor:
            print("Erro! Não pode fazer saque maior que limite.")

        elif numero_saques >= 3:
            print("Erro! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"\nSaque: R$ {valor:.2f}"
            numero_saques += 1

        else:
            print(f"Erro! SAQUE {valor} Invalido.")

    elif opcao == "E":
        if(extrato != ""):
            print(f"EXTRATO. {extrato}/n Fim EXTRATO")
        else:
            print("Sem EXTRATO.")
    elif opcao == "Q":
        break
    else:
        print("Erro. Escolha a opção ||===>>[Q]<<=====SAIR============|| ")