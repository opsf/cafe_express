import os

restaurantes = [{'nome':'Comedere', 'categoria': 'Selve service', 'ativo': True},{
                'nome':'Vem Que Tem', 'categoria': 'pizza', 'ativo': False},{
                'nome':'La Carte', 'categoria': 'suchi', 'ativo': False }]

def exibir_nome():
    print("""
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n""")

def exibir_opcoes():    
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair restaurante\n')

def voltar_menu_principal():
    input('Digite enter para voltar ao menu principal  ')    
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def finalizar_app():
    exibir_subtitulo('Encerrando o programa')
    
def opcao_invalida():
    exibir_subtitulo('opção inválida ')
    voltar_menu_principal()

def cadastro_novo_restaurante():
    exibir_subtitulo('Cadastro de novo restaurante\n')    
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_menu_principal()

def lista_restaurante():
    exibir_subtitulo('Listando restaurantes\n')    
    for restaurante in restaurantes:        
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'{nome_restaurante}    |    {categoria}   |   {ativo}')
    voltar_menu_principal()



def escolher_opcoes(): 
    try:   
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida==1:
            cadastro_novo_restaurante()
        elif opcao_escolhida==2:
            lista_restaurante()
        elif opcao_escolhida==3:
            print('Ativar restaurante')
        elif opcao_escolhida==4:
            print('Encerrando o programa')
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcoes()

if __name__=='__main__':
    main()

