import os

restaurante = ['Pizza', 'Lasanha']

def exibir_nome():
    print("""
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair restaurante\n')

def finalizar_app():
    os.system('cls')
    print('Encerrando o programa')

def opcao_invalida():
    print("Opção inválida\n")
    input('Aperte qualquer tecla para voltar')
    main()

def cadastro_novo_restaurante():
    os.system('cls')
    print('Cadastro de novo restaurante\n')
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    restaurante.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    input('Digite enter para voltar ao menu principal  ')
    main()

def lista_restaurante():
    os.system('cls')
    print('Listando restaurantes\n')
    for resta in restaurante:
        print(resta)    
    input('\nDigite enter para voltar ao menu principal  ')
    main()



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

