p1 = {
    'Valor': 300,
    'Desconto': 0,
    'Valor Final': 0
}

desconto = int(input('Digite o desconto: '))

p1.update(Desconto=desconto)
if desconto <= 100:
    promocao = (p1['Valor'] * desconto) / 100
    valortotal = p1['Valor'] - promocao
    p1.update({'Valor Final': valortotal})
    print(p1)
else:
    print('Erro no desconto')