from datetime import datetime


menu = """
[d] Depositar
[s] Sacar 
[e] Extrato 
[q] sair 
==>> """

saldo = 0
numero_saques = 0
limite = 500
extrato = []
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).casefold()
    
    if opcao == "d":
        operacao = 'Deposito'
        valor = float(input('Favor insera o valor que deseja depositar R$ '))
        while valor <=0:
            print('Esse valor não é permitido, favor insera um valor positivo.')
            valor = float(input('Favor insera o valor que deseja depositar R$ '))
        saldo += valor
        dia = datetime.now()
        data = dia.strftime("%d") +"/"+ dia.strftime("%m") +"/"+ dia.strftime("%y")
        extrato.append(f'{data} {operacao} R${valor}')
        print(f"Seu valor R${valor} foi depositado com sucesso")
    elif opcao == "s":
        print("Saque")
    elif opcao == "e":
        print(extrato)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")