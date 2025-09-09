agenda = {}
while True:
    print('----Agenda de Contatos----')
    print('1. Adicionar Contato')
    print('2. Listar Contatos')
    print('3. Buscar Contatos')
    print('4. Remover Contato')
    print('5. Sair')
    print('--------------------------')


    opcao = input('Escolha uma opção')

    if opcao == '1':
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        agenda[nome] = telefone
        print(f'Contato {nome} adiconado com sucesso!')
    
    elif opcao == '2':
        print("----Lista de Contatos----")
        if agenda:
            for nome, telefone in agenda.items():
                print(f'Nome: {nome} | Telefone: {telefone}')
        else:
            print('A agenda de contatos está vazia.')

    elif opcao == '3':
        print("-> Buscar Contato")
        nome_busca = input('Digite o nome do contato que deseja buscar: ')

        if nome_busca in agenda:
            print("--- Contato Encontrado ---")
            print(f"Nome: {nome_busca} | Telefone: {telefone}")
        else:
            print(f"Contato '{nome_busca}' não foi encontrado na agenda.")


    elif opcao == '4':
        print("-> Remover Contato")
        nome_remover = input('Digite o nome do contato que deseja remover: ')

        if nome_remover in agenda:
            del agenda[nome_remover]
            print(f'Contato {nome_remover} foi removido com sucesso!')

    elif opcao == '5':
        print('Obrigado por usar a agenda. Até logo!')

        break
    else:
        print('Opção inválida. Por favor, escolha um numero de 1 a 5.')
