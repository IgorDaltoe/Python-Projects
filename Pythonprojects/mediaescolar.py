nome = input('Qual o nome do aluno ? ').strip().title()
série = int(input('Qual a série do aluno ? ')).strip()
nota1 = float(input('Qual a nota do primeiro trimestre ? ')).strip()
nota2 = float(input('Qual a nota do segundo trimestre ? ')).strip()
nota3 = float(input('Qual a nota do terceiro trimeestre ? ')).strip()
media = ((nota1 * 1) + (nota2 * 2) + (nota3 * 3)) / (1 + 2 + 3)
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'vermelho' : '\033[31m',
         'verde' : '\033[32m'}
print('Aluno: {}'.format(nome))
print('Série: {}º'.format(série))
print('Sua média foi {}{:.1f}{}!'.format(cores['verde'], media, cores['limpa']))
if media > 7:
    print('{}PARABÉNS! VOCÊ PASSOU DE ANO!{}'.format(cores['azul'], cores['limpa']))
else:
    print('{}VOCÊ NÃO PASSOU DE ANO!{}'.format(cores['vermelho'], cores['limpa']))