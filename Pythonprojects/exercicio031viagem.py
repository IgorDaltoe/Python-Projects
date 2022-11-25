print('Bem Vindo(a) Cidade1!')
nome = str(input('Qual o seu nome ? ')).title().strip()
print('Temos viagens para:\nCidade2 207Km\nCidade3 375Km\nCidade4 420Km\nCidade5 220Km')
A = int(input('Qual a distancia da cidade que você deseja viajar ? '))
if A == 207:
    C = str('Cidade2')
elif A == 375:
    C = str('Cidade3')
elif A == 420:
    C = str('Cidade4')
elif A == 220:
    C = str('Cidade5')
else:
    C = str('Cidade Inexistente')
if A >= 375:
    passagem = A * 0.60
else:
    passagem = A * 0.50
print('Passageiro: {}'.format(nome))
print('Viage: de Cidade1 para {}'.format(C))
print('Custo da passagem: R${:.2f}.'.format(passagem))
print('Boa Viagem!')
