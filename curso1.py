import os

restaurantes = [{
    'nome': 'burgman',
    'categoria': 'bar',
    'ativo': False
},{
    'nome': 'sr.myag',
    'categoria': 'japones',
    'ativo': True
}]

def exibe_nome_app():
    print('Ϩⲁⲃⲟꞅ Ⲉⲭⲣꞅⲉ𝛓𝛓\n')

def voltar_menu():
    input('Digite uma tecla para retornar: ')
    os.system('cls')
    main()    

def exibir_subtitulo(subtitulo) -> str:
    os.system('cls')
    print(f'{subtitulo} \n')
        

def cadastrar_restaurante():
    exibir_subtitulo('Cadastrar restaurantes:')
    nome = input('Digite o nome do restaurante a cadastrar: ')
    categoria = input(f'Digite a categoria do restaurnte {nome}: ')
    dados = {'nome': nome, 'categoria' : categoria, 'ativo': False}
    print(f'O restaurante {nome} foi cadastrado com sucesso!!')
    restaurantes.append(dados)
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes:')
    print(f'{'Restaurantes:'.ljust(21)} | {'Categorias:'.ljust(21)} | {'Estado:'}')
    for restaurante in restaurantes:
        print(f'-{restaurante['nome'].ljust(20)} | -{restaurante["categoria"].ljust(20)} | -{'ativado' if restaurante["ativo"] else 'desativado'}')
    voltar_menu()

def altera_estado_restaurante():
    exibir_subtitulo('Alterar o estado do restaurante: ')

    nome_restaurante = input('Digite o nome do restaurante que deseja altera o estado: ').lower()
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            estado = 'Ativado' if restaurante['ativo'] else 'Desativado'
            mensagem = f'O restaurante {nome_restaurante} teve seu estado alterado para {estado}.'
            print(mensagem)
            break
        
    if restaurante_encontrado == False:
        print(f'O restaurante {nome_restaurante} não foi encontrado, tente novamente!')

    voltar_menu()

def opcao_invalida():
    print('Opcao invalida...')
    voltar_menu()   

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. sair\n')

def escolhe_opcao():
    try:
        escolha = int(input('Digite uma opcao: '))

        if escolha == 1:
            cadastrar_restaurante()
        elif escolha == 2:
            listar_restaurantes()
        elif escolha == 3:
            altera_estado_restaurante()
        elif escolha == 4:
            exibir_subtitulo('Encerrando programa...')
        else:
            opcao_invalida()
    except:
        opcao_invalida()            


def main():
    exibe_nome_app()
    exibir_opcoes()
    escolhe_opcao()

if __name__ == '__main__':  
    main()  