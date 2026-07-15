# Agenda de contatos
contatos = []
def ler_int(valor):
    while True:
        try:
            numero = int(input(valor))
            return numero
        except ValueError:
            print("Por favor, digite um número válido!")

def adicionar():
    global contatos
    nome = input('nome: ').strip()
    telefone = input('telefone: ').strip()
    email = input('email: ').strip()
    contato = {'nome': nome, 'telefone': telefone, 'email': email}
    contatos.append(contato)
    print('Contato adicionado com sucesso!')

def visualizar():
    global contatos
    if not contatos:
        print('Nenhum contato foi encontrado.')
        return
    for contato in contatos:
        for chave, valor in contato.items():
            print(f'{chave}: {valor}')
            print("-----")

def pesquisar():
    termo = input('Digite o nome, telefone e email para pesquisar: ').strip().lower()
    encontrado = []
    for contato in contatos:
        if termo in contato['nome'].lower() or termo in contato['telefone'].lower() or termo in contato['email'].lower():
            encontrado.append(contato)
    if not encontrado:
        print('Nenhum contato foi encontrado!')
    else:
        for contato in encontrado:
            for chave, valor in contato.items():
                print(f'{chave}: {valor}')
                print("-----")

def mini_menu():
    print('''
    1) Nome
    2) Telefone
    3) Email
    ''')
    escolha = ler_int("Qual campo deseja alterar? ")
    return escolha

def editar():
    termo = input('Digite o nome, telefone e email para pesquisar: ').strip().lower()

    encontrado = []
    for contato in contatos:
        if termo in contato['nome'].lower() or termo in contato['telefone'].lower() or termo in contato['email'].lower():
            encontrado.append(contato)

    if len(encontrado) == 0:
        print('Nenhum contato foi encontrado!')
        return

    if len(encontrado) == 1:
        contato = encontrado[0]
    else:
        identificador = input('Mais de um contato encontrado. Digite o telefone ou email exato: ').strip().lower()
        contato_certo = []
        for c in encontrado:
            if c['telefone'].lower() == identificador or c['email'].lower() == identificador:
                contato_certo.append(c)

        if len(contato_certo) != 1:
            print('Não foi possível identificar um único contato!')
            return
        contato = contato_certo[0]
    while True:
        campo = mini_menu()
        if campo in [1,2,3]:
            break
        print("Opção inválida! Escolha 1, 2, 3.")
    if campo == 1:
        novo_nome = input('Novo nome: ').strip()
        contato['nome'] = novo_nome
    elif campo == 2:
        novo_telefone = input('Novo telefone: ').strip()
        contato['telefone'] = novo_telefone
    elif campo == 3:
        novo_email = input('Novo email: ').strip()
        contato['email'] = novo_email

    print('Contato atualizado com sucesso!')


def remover():
    termo = input ('Digite o nome, telefone e email para remover: ').strip().lower()
    encontrado = []
    for contato in contatos:
        if termo in contato['nome'].lower() or termo in contato['telefone'].lower() or termo in contato['email'].lower():
            encontrado.append(contato)
    if len(encontrado) == 0:
        print('Nenhum contato foi encontrado!')
        return

    if len(encontrado) == 1:
        contato = encontrado[0]
    else:
        identificador = input('Mais de um contato encontrado. Digite o telefone ou email exato: ').strip().lower()
        contato_certo = []
        for c in encontrado:
            if c['telefone'].lower() == identificador or c['email'].lower() == identificador:
                contato_certo.append(c)

        if len(contato_certo) != 1:
            print('Não foi possível identificar um único contato!')
            return
        contato = contato_certo[0]


    confirmaçao = input(f'Tem certeza que deseja remover o contato {contato["nome"]}? (s/n) ').strip().lower()
    if confirmaçao in ['s','sim']:
        contatos.remove(contato)
        print('Contato removido com sucesso!')
    elif confirmaçao in ['n','nao', 'não']:
        print('Remoção cancelada!')
    else:
        print('Opção inválida!')



# menu
def menu():
    while True:
        print('''
        1) Adicionar Contatos
        2) Remover Contatos
        3) Visualizar Contatos
        4) Pesquisar Contatos
        5) Editar Contatos
        0) Sair do Programa
        ''')
        escolha = ler_int("Escolha uma opção: ")
        if escolha == 1:
            adicionar()
        elif escolha == 2:
            remover()
        elif escolha == 3:
            visualizar()
        elif escolha == 4:
            pesquisar()
        elif escolha == 5:
            editar()
        elif escolha == 0:
            break

menu()
























































