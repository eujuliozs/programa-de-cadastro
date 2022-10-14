from corpo import *
from time import sleep

cabecalho('cadastro')
menu = ['cadastrar pessoas','ver pessoas cadastradas','sair do programa']
while True:
    for p,c in enumerate(menu):
        print(p+1, c)
    print(linha())
    opcao_usuario = opcMenu('qual seria a sua opção? ')
    print(linha())
    if opcao_usuario == 1:
        while True:
            registrar()
            e = opcontinue('deseja continuar [s/n]?')
            if e == 'n':
                print(linha())
                sleep(0.4)
                break
    if opcao_usuario == 3:
        print('\033[1;36m VOLTE SEMPRE!\033[m')
        print(linha())
        sleep(0.4)
        break
    if opcao_usuario == 2:
        cadastrados()
        print(linha())
        sleep(0.4)

    


