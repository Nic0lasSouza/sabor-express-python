import os

restaurantes = [
    {'nome':'praça', 'categoria':'japonesa', 'ativo':False},
    {'nome':'pizza suprema', 'categoria':'pizza', 'ativo':True},
    {'nome':'cantina', 'categoria':'italiano', 'ativo':False}]

def exibir_nome_programa():
    '''Exibe o nome estilizado do programa'''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def exibir_opcoes():
    print('1-Cadastrar Restaurante')
    print('2-Listar Restaurante')
    print('3-Alternar espaço do  Restaurante')
    print('4-Sair\n')

def finalizar_app():
    exbir_subtitulos('Finalizando o app')

def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante
    Inputs:
    - Nome do restaurante
    - Categoria
    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exbir_subtitulos('Cadastro de novos restaurantes')
    nome_do_restaurante=input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_restaurante = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria_restaurante,
        'ativo': False
        }
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante {nome_do_restaurante} cadastrado com sucesso!!!\n')
    voltar_ao_menu()

def opcao_invalida():
    print('Opção Invalida!\n')
    voltar_ao_menu()

def exbir_subtitulos(texto):
    os.system('cls')
    linha = '*' *(len(texto) + 2)
    print(linha)
    print(texto)
    print(linha)
    print()

def listar_restaurante():
    exbir_subtitulos('Listando um restaurante')
    print(f'{'Nome do restaurnate'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante ='ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')

    voltar_ao_menu()

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def alternar_estado_restaurante():
    exbir_subtitulos('Alterando estado do restaurante')
    nome_restaurante = input('Dígite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado= False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mesagem= f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mesagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurante()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()

    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()