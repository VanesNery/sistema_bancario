'''
    Operação de deposito
    Dever ser possivel valores positivos, com apenas 1 usuario, sem se preocupar com agwencia we conta. Todos depositos devem ser armazenados em uma variavel e exibido na operação de extrato
'''
def deposito(data, operacao, extrato, saldo, valor):
    while valor <=0:
        print('Esse valor não é permitido, favor insera um valor positivo.')
        valor = float(input('Favor insera o valor que deseja depositar R$ '))
    saldo += valor
    print(f"Seu valor R${valor} foi realizado o {operacao} com sucesso")
    return extrato.append(f'{data} {operacao} R${valor}')
