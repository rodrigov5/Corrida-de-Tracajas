quantidade = float(input("Digite quantos tracajas irao participar: "))

nivel1 = []
nivel2 = []
nivel3 = []

count = 0

while count < quantidade:
    count += 1

    velocidade = int(input(f'Digite a velocidade do tracaja {count}: '))

    if velocidade <= 25:
        if velocidade < 10:
            nivel1.append(velocidade)
        elif velocidade >= 10 and velocidade < 15:
            nivel2.append(velocidade)
        elif velocidade >= 15:
            nivel3.append(velocidade)
    else:
        print('Velocidade muito alta.')
        count = 0

    if velocidade == 0:
        print('Velocidade igual a zero, terminando programa!')
        break

def checaVelocidade(array):
    maximo = array[0]
    for i in range(len(array)):
        if array[i] > maximo:
            maximo = array[i]
    return maximo

print(f'''
Nivel 1 ==== {nivel1}
Nivel 2 ==== {nivel2}
Nivel 3 ==== {nivel3}
''')

if len(nivel1) > 0:
    print(f'Tracaja mais veloz do nível 1: {checaVelocidade(nivel1)}')
else:
    print('Sem participantes no nivel 1')

if len(nivel2) > 0:
    print(f'Tracaja mais veloz do nível 2: {checaVelocidade(nivel2)}')
else:
    print('Sem participantes no nivel 2')

if len(nivel3) > 0:
    print(f'Tracaja mais veloz do nível 3: {checaVelocidade(nivel3)}')
else:
    print('Sem participantes no nivel 3')
