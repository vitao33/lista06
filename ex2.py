qtde_internet = int(input('Informe o consumo de internet: '))
qtde_local = int(input('Informe o consumo de ligação locais: '))
qtade_interubano = int(input('Informe o consumo de ligações interubano: '))
qtade_torpedo = int(input('Informe o consumo de torpedo: '))

valor_internet = qtde_internet * 0.5
valor_local = qtde_local * 0.35
valor_interubano = qtade_interubano * 0.6
valor_torpedo = qtade_torpedo * 0.2

total_sem_desconto = valor_internet + valor_local + valor_interubano + valor_torpedo

if qtde_internet > 50:
    desconto_internet = valor_internet * 0.05
else:
    qtde_internet = 0

if qtde_local > 200:
    desconto_local = valor_local * 0.1
else:
    desconto_internet = 0

if qtade_interubano > 150:
    desconto_interubano = valor_interubano * 0.1
else:
    qtade_interubano = 0

if qtade_torpedo > 50:
    desconto_torpedo = valor_torpedo * 0.2
else:
    qtade_torpedo = 0

if desconto_internet > desconto_local and\
    desconto_internet > desconto_interubano and\
    desconto_internet > desconto_torpedo:
    print('O desconto será sobre o serviço internet')
    print(f'O valor de desconto sera R$ {desconto_internet:.2f}')
elif desconto_local > desconto_internet and\
    desconto_local > desconto_interubano and\
    desconto_local > desconto_torpedo:
    print('O desconto será sobre o serviço local')
    print(f' O valor de desconto sera R$ {desconto_local:.2f}')
elif desconto_interubano > desconto_internet and\
     desconto_interubano > desconto_local and\
    desconto_interubano > desconto_torpedo:
    print('O desconto sera sobre o serviço interubano')
    