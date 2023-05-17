from datetime import datetime
from deposito import deposito
from extrato import extrat
from saque import saque


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

while True:
    opcao = input(menu).casefold()
    dia = datetime.now()
    data = dia.strftime("%d") +"/"+ dia.strftime("%m") +"/"+ dia.strftime("%y")
    
    if opcao == "d":
        operacao = 'Deposito'
        valor = float(input('Favor insera o valor que deseja depositar R$ '))
        saldo_final = deposito(data, operacao, saldo, extrato, valor)
        saldo = saldo_final
    elif opcao == "s":
        operacao = 'Saque'
        valor = float(input('Favor insera o valor que deseja sacar R$ '))
        saldo_final, numero = saque(valor, limite, saldo, data, extrato, numero_saques, operacao)
        saldo = saldo_final
        numero_saques = numero
    elif opcao == "e":
        extrat(extrato, saldo)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")