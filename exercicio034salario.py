nome = input('Digite o nome do funcionário: ').strip().title()
salário = float(input('Digite o salário do funcionário: R$'))
anos = int(input('Digites quantos ano o funcionário está na empresa: '))
cargo = input('Digite o cargo do funcionario: ').strip().title()
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarela' : '\033[33m',
         'verde' : '\033[32m'}
if salário <= 1000 and anos > 5:
    aumento = salário * 15 / 100
    aumt = 15
elif salário <= 1000:
    aumento = salário * 10 / 100
    aumt = 10
else:
    aumento = salário * 5 / 100
    aumt = 5
print('O funcionário {7}{0}{6} trabalha como {7}{1}{6} a {7}{2}{6} anos, recebe {8}R${3:.2f}{6} e terá um aumento de {9}{4}%{6}. Seu novo salário será {9}R${5:.2f}{6}! '.format(nome, cargo, anos, salário, aumt, salário + aumento, cores['limpa'], cores['azul'], cores['amarela'], cores['verde']))