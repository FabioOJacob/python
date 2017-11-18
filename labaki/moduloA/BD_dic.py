# Desenvolva um banco de dados simples de forma que o usuário possa inserir um produto e seu preço,
# além de poder consultar o preço de um produto, tudo isso sem acessar o arquivo de texto.


bd = {}
sair = False

while sair == False:
    print('Banco de dados de Produtos')
    print('')
    choice = str(input('(S)SAIR, (I)INSERIR, (C)CONSULTAR, (T)LISTAR TUDO: ')).upper()
    if choice == 'S':
        sair = True

    elif choice == 'I':
        print('')
        prod = str(input('Insira o produto: '))
        custo = float(input('Qual o valor de {}: '.format(prod)))
        bd[prod] = custo
        print('')
        print('Item cadastrado com sucesso!!\n')

    elif choice == 'C':
        print('')
        cons = str(input('Insira o nome do produto que deseja consultar: '))
        verif = cons in bd
        if verif:
            print('')
            print('{} custa R$ {:.2f}.'.format(cons, bd[cons]))
            print('')
        else:
            print('*** {} não existe no cadastro. ***\n'.format(cons.upper()))

    elif choice == 'T':
        print('')
        if len(bd) == 0:
            print('Cadastro VAZIO.\nInsira pelo menos um item para consultar.\n')
        else:
            print('-' * 20)
            for i in bd:
                print('{} custa R$ {:.2f}.'.format(i.upper(), bd[i]))
            print('')
            print('-' * 20)
    else:
        print('\n****** Digite uma opção válida! ******\n')