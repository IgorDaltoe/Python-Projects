print('Vamos tentar formar um triângulo! Digite o comprimento de 3 semirretas ')
A = float(input('Primeira semirreta: '))
B = float(input('Segunda semirreta: '))
C = float(input('Terceira semirreta: '))
cores = {'limpa' : '\033[m',
         'verde' : '\033[34m',
         'vermelho' : '\033[31m'}
retas = [A, B, C]
retas.sort()
menor = retas[0] + retas[1]
maior = retas [2]
if menor > maior:
    print('Essas semirretas {}conseguem formar um triângulo!{}'.format(cores['verde'], cores['limpa']))
else:
    print('Essas semirretas {}não conseguem formar um triângulo!{}'.format(cores['vermelho'], cores['limpa']))