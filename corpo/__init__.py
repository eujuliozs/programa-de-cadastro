def linha(tam=40):
    return '='*tam

def opcontinue(msg):
    while True:
        e = str(input(msg))
        if e == '':
            print('Erro.', end='')

        try:
            e = e.strip().lower()[0]
        except:
            print('opçao invalida')
        else:
            if e in 'sn':
                return e

def opcMenu(msg):
    while True:
        option = LeiaInt(msg)
        if option == 1:
            return option
        if option == 2:
            return option
        if option == 3:
            return option
        else:
            print('\033[1;31mErro! opção invalida\033[m')

def LeiaInt(msg):
    verify = False
    while True:
        try:
            i = int(input(msg))
        except:
            print(f'\033[1;31mErro! por favor digite um numero inteiro valido valido\033[m')
        else:
            return i

def cabecalho(msg, tam=40):
    print('='*tam)
    print('{:^40}'.format(msg))
    print('='*tam)

def registrar():
    import mysql.connector
    
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='10032005Jc%',
        database='novo'
    )
    mycursor = db.cursor()

    try:
        nome = input('Nome?: ')
    except:
        print('Digite um nome valido')
    else:
        idade = LeiaInt('Idade: ')
        mycursor.execute('INSERT INTO cadastro (nome, idade) VALUES(%s, %s)',(nome, idade))
        db.commit()

def cadastrados():
    import mysql.connector
    e = linha(1)
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='10032005Jc%',
        database='novo'
    )
    mycursor = db.cursor()
    print('temos alguns filtros, esta interessado? ')
    opcao_usuario = opcontinue('[s/n]')
    if opcao_usuario == 'n':
        mycursor.execute('SELECT nome, idade FROM cadastro')
        for c in mycursor:
            print(f'nome: {c[0]} {e} {c[1]} anos')
    else:
        print('1 - idade decrescente \n2 - idade crescente')
        while True:
            filtro = LeiaInt('sua opção:')
            if filtro == 1 or filtro == 2:
                break
            else:
                print('\033[mdigite uma opção valida\033[m')
        print(linha())
        if filtro == 1:
            mycursor.execute('SELECT nome, idade FROM cadastro ORDER BY idade DESC')
            for g in mycursor:
                print(f'nome: {g[0]} {e} {g[1]} anos')
        if filtro == 2:
            mycursor.execute('SELECT nome, idade FROM cadastro ORDER BY idade ASC')
            for f in mycursor:
                print(f'nome: {f[0]} {e} {f[1]} anos')
    


