import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

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
   sub_titulo('Finalizando o programa...')
    


def opcao_invalida():
    print('Opção inválida! Tente novamente.\n')
    voltar_menu()

def alterar_status():
    sub_titulo('Alterando status do restaurante...')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja alterar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante.lower() == restaurante['nome'].lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f"Status do restaurante '{nome_do_restaurante}' foi ativado com sucesso." if restaurante['ativo'] else f"Status do restaurante '{nome_do_restaurante}' foi desativado com sucesso."
            print(mensagem)
            

    if not restaurante_encontrado:
        print(f"Restaurante '{nome_do_restaurante}' não encontrado.")
    

    voltar_menu()

def escolher_opcao(opcao_escolhida):
    try:
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
           alterar_status()
        elif opcao_escolhida == 4:
            finalizar()
        else:
            opcao_invalida()

    except ValueError:
        opcao_invalida()
    
    opcao_escolhida = int(input('Escolha uma opção: '))
    print(f"Você escolheu a opção {opcao_escolhida}")
    escolher_opcao(opcao_escolhida)

def sub_titulo(texto):
    os.system("cls")
    linha = "*" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print("")

def cadastrar_restaurante():
    sub_titulo('Cadastrando restaurante...')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_restaurante = input(f'Digite a categoria do restaurante: {nome_do_restaurante} ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'Restaurante "{nome_do_restaurante}" cadastrado com sucesso!')
    voltar_menu()

def listar_restaurantes():
    sub_titulo('Listando restaurantes...')
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo_restaurante = restaurante["ativo"]
        print(f"- {nome_restaurante} / {categoria_restaurante} / {ativo_restaurante}")

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
