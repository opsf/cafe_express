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

def escolher_opcoes():    
    opcao_escolhida = int(input('Digite uma opção: '))
    if opcao_escolhida==1:
        print('Cadastrar restaurante')
    elif opcao_escolhida==2:
        print('Listar restaurante')
    elif opcao_escolhida==3:
        print('Ativar restaurante')
    else:
        finalizar_app()

def main():
    exibir_nome()
    exibir_opcoes()
    escolher_opcoes()




if __name__=='__main__':
    main()

