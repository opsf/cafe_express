import os

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


def escolher_opcoes(): 
    try:   
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida==1:
            print('Cadastrar restaurante')
        elif opcao_escolhida==2:
            print('Listar restaurante')
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

