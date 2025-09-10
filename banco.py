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

    if opcao == "d":
        valor = float(input("Informe o valor do saque: "))
        print(f"Deposito {valor}.")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        print(f"Saque {valor}.")
    elif opcao == "e":
        print("Extrato.")
    elif opcao == "q":
        break
    else:
        print("Erro.")