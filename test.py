print('bem-vindo a loja de gelados do david')
tam = 20
line = '-'
print(f'  + {line * tam} cardápio {line * tam} +')
print(f'  {line * 53}')
print(f'{line * 3}|     TAMANHO     |    CUPUAÇU (CP)   | AÇAÍ (AC) |{line * 3}')
print('---|       P         |      R$ 9,00      |  R$ 11,00 |---')
print('---|       M         |      R$ 14,00     |  R$ 16,00 |---')
print('---|       G         |      R$ 18,00     |  R$ 20,00 |---')
print(f'  {line * 53}')

# Solicita o sabor

sabor = input('Escolha o sabor desejado (CP/AC): ')

while sabor not in ('CP', 'AC'):
    print('Sabor inválido. Tente novamente')
    sabor = input('Escolha o sabor desejado (CP/AC): ')

# Solicita o tamanho

tamanho = input('Escolha o tamanho (P/M/G): ')

while tamanho not in ('P', 'M', 'G'):
    print("Tamanho inválido. Tente novamente")

    tamanho = input('Escolha o tamanho (P/M/G): ')

# Calcula o valor do pedido

if sabor == 'CP':

    if tamanho == 'P':
        valor = 9

    elif tamanho == 'M':
        valor = 14

    else:
        valor = 18

else:

    if tamanho == 'P':
        valor = 11

    elif tamanho == 'M':
        valor = 16

    else:
        valor = 20
# Acumulador para somar os valores dos pedidos

total = 0

# Pergunta se o cliente deseja pedir mais

pedido = input('Deseja pedir mais alguma coisa? (S/N): ')

while pedido == 'S':

    # Solicita o sabor

    sabor = input('Escolha o sabor desejado (CP/AC): ')

    while sabor not in ('CP', 'AC'):
        print('Sabor inválido. Tente novamente')

        sabor = input('Escolha o sabor desejado (CP/AC): ')

    # Solicita o tamanho

    tamanho = input('Escolha o tamanho (P/M/G): ')

    while tamanho not in ("P", "M", "G"):
        print('Tamanho inválido. Tente novamente')

        tamanho = input('Escolha o tamanho (P/M/G): ')

    # Calcula o valor do pedido

    if sabor == 'CP':

        if tamanho == 'P':
            valor1 = 9

        elif tamanho == 'M':
            valor1 = 14

        else:
            valor1 = 18

    else:

        if tamanho == 'P':
            valor1 = 11

        elif tamanho == 'M':
            valor1 = 16

        else:
            valor1 = 20

    # Acumulador para somar os valores dos pedidos

    total = valor + valor1

    # Pergunta se o cliente deseja pedir mais

    pedido = input('Deseja pedir mais alguma coisa? (S/N): ')

# Exibe o total dos pedidos

print(f'O valor total a ser pago é R$ {total}')
