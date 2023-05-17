'''
    Operação de Saque
    Deve permitir realizer 3 saques diarios com limite de 500,00 por saque. Caso usuario não tenha saldo em conta, deve exibir mensagem de nãp será possivel sacar o dinheiro pór falta de saldo. Todos os saques devem ser armazenados em uma variavel e exibidos na operação extrato
'''
LIMITE_SAQUES = 3
def saque(valor, limite, saldo, data, extrato, numero_saques, operacao):
    while valor > limite:
        print(f'Valor não permitido para saque, o limite para saque nesse momento é de R$ {limite}')
        valor = float(input('Favor insera o valor que deseja sacar R$ '))
    if valor <= saldo and numero_saques < LIMITE_SAQUES:
        saldo -= valor
        numero_saques += 1
        extrato = extrato.append(f'{data} {operacao} R${valor}')
        print(f"Seu valor R${valor} foi liberad para {operacao}")
    elif valor > saldo:
        print(f'Seu saldo é menor que solicitado para {operacao}')
    else:
        print('Você já passou o limite de saques diario')
    return saldo, numero_saques
