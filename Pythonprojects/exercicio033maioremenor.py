A = int(input('Digite um valor: '))
B = int(input('Digite um segundo valor: '))
C = int(input('Digite um terceiro valor: '))
D = int(input('Digite um quarto valor: '))
num = [A, B, C, D]
num.sort()
print(' \033[34m O maior valor é {}.\033[m '.format(max(num)))
print(' \033[32m O menor valor é {}.\033[m '.format(min(num)))
