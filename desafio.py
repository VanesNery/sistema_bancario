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
    dia = datetime.now()
    data = dia.strftime("%d") +"/"+ dia.strftime("%m") +"/"+ dia.strftime("%y")
    
    if opcao == "d":
        operacao = 'Deposito'
        valor = float(input('Favor insera o valor que deseja depositar R$ '))
        while valor <=0:
            print('Esse valor não é permitido, favor insera um valor positivo.')
            valor = float(input('Favor insera o valor que deseja depositar R$ '))
        saldo += valor
        extrato.append(f'{data} {operacao} R${valor}')
        print(f"Seu valor R${valor} foi realizado o {operacao} com sucesso")
    elif opcao == "s":
        operacao = 'Saque'
        valor = float(input('Favor insera o valor que deseja sacar R$ '))
        while valor > limite:
            print(f'Valor não permitido para saque, o limite para saque nesse momento é de R$ {limite}')
            valor = float(input('Favor insera o valor que deseja sacar R$ '))
            if valor <= saldo:
                saldo -= valor
                extrato.append(f'{data} {operacao} R${valor}')
                print(f"Seu valor R${valor} foi realizado o {operacao} com sucesso")
            else:
                print('Seu saldo é menor que solicitado para {operacao}')
    elif opcao == "e":
        print(extrato)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")