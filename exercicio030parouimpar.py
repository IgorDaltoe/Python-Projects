n = int(input('Digite um número: '))
conta = n % 2
if conta == 0:
    print('\033[32mO número {} é PAR\033[m'.format(n))
else:
    print('\033[31mO número {} é IMPAR\033[m'.format(n))
