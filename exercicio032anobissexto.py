from datetime import date
ano = int(input('Digite 0 para o ano atual ou digite um ano: '))
cores = {'limpa' : '\033[m', 
            'azul' : '\033[34m',
            'amarelo' : '\033[33m',}

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {0}{1}{2} é um ano {0}bissexto{2}'.format(cores['azul'],ano, cores['limpa']))
else:
    print('O ano {0}{1}{2} não é um ano {0}bissexto{0}'.format(cores['amarelo'], ano, cores['limpa']))
