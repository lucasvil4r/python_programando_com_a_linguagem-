inventario = []
resp = 'S'
#função .append adicionar dados dentro da lista.
while (resp == 'S'):
    inventario.append(str(input('Equipamento: ')))
    inventario.append(float(input('Valor: R$ ')))
    inventario.append(int(input('NSerial: ')))
    inventario.append(input('Dept: '))
    resp = input('Digite \"S\" para continuar: ').upper()