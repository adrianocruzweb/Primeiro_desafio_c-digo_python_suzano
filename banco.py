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
            extrato += f"DEPÓSITO: R$ {valor:.2f}\n"

        else:
            print(f"Erro no depósito! Valor: {valor} inválido.")
    elif opcao == "S":
        valor = float(input("Informe o valor do SAQUE: "))
        print(f"SAQUE {valor}.")
    elif opcao == "E":
        if(extrato != ""): print(f"EXTRATO. {extrato}")
        print("Sem EXTRATO.")
    elif opcao == "Q":
        break
    else:
        print("Erro. Escolha a opção ||===>>[Q]<<=====SAIR============|| ")