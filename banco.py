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
        valor = float(input("Informe o valor do DEPOSITO: "))
        print(f"DEPOSITO {valor}.")
    elif opcao == "S":
        valor = float(input("Informe o valor do SAQUE: "))
        print(f"SAQUE {valor}.")
    elif opcao == "E":
        print("EXTRATO.")
    elif opcao == "Q":
        break
    else:
        print("Erro. Escolha a opção ||===>>[Q]<<=====SAIR============|| ")