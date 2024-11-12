import hashlib

sair = ''
while(sair != 'S'):

    string = input('Olá, Escreva algo que eu irei gerar sua hash.')

    hash = hashlib.sha1(string.encode())

    print(f'Hash gerada: {hash.hexdigest()}')

    sair = input('Deseja sair [S]im ou [N]ão: ').upper()