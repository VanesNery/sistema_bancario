'''
    Operação extrato
    Deve listrar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. No formato R$ xxx.xx
'''
def extrat(extrato, saldo):
    print('Extrato')
    for registro in extrato:
        print(registro)
    print(f'Valor atual: R${saldo}')
