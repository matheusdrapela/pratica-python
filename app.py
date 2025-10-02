import os

restaurantes = ["pizza", "hamburguer"]

def exibir_tela_inicial():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)


def exibir_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar():
    os.system("cls")
    print('Finalizando o programa \n')
    


def opcao_invalida():
    print('Opção inválida! Tente novamente.\n')
    voltar_menu()



def escolher_opcao(opcao_escolhida):
    try:
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativando restaurante...')
        elif opcao_escolhida == 4:
            finalizar()
        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()
    
    opcao_escolhida = int(input('Escolha uma opção: '))
    print(f"Você escolheu a opção {opcao_escolhida}")
    escolher_opcao(opcao_escolhida)

def cadastrar_restaurante():
    os.system("cls")
    print('Cadastrando restaurante...')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'Restaurante "{nome_do_restaurante}" cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    os.system("cls")
    print('Listando restaurantes...')
    for restaurante in restaurantes:
        print(f"- {restaurante}")

    voltar_menu()

def voltar_menu():
    input("digite uma tecla para recomeçar")
    main()

def main():
    os.system("cls")
    exibir_tela_inicial()
    exibir_menu()
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f"Você escolheu a opção {opcao_escolhida}")
        escolher_opcao(opcao_escolhida)
    except ValueError:
        opcao_invalida()


if __name__ == "__main__":
    main()
